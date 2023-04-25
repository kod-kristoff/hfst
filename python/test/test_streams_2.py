# -*- coding: utf-8 -*-
import sys
if len(sys.argv) > 2:
    sys.path.insert(0, sys.argv[2])
import hfst
if len(sys.argv) < 1:
    raise RuntimeError('Transducer format must be given as first argument')

if sys.argv[1] == 'sfst':
    if not hfst.HfstTransducer.is_implementation_type_available(hfst.ImplementationType.SFST_TYPE):
        sys.exit(77)
    hfst.set_default_fst_type(hfst.ImplementationType.SFST_TYPE)
elif sys.argv[1] == 'foma':
    if not hfst.HfstTransducer.is_implementation_type_available(hfst.ImplementationType.FOMA_TYPE):
        sys.exit(77)
    hfst.set_default_fst_type(hfst.ImplementationType.FOMA_TYPE)
elif sys.argv[1] == 'openfst':
    if not hfst.HfstTransducer.is_implementation_type_available(hfst.ImplementationType.TROPICAL_OPENFST_TYPE):
        sys.exit(77)
    hfst.set_default_fst_type(hfst.ImplementationType.TROPICAL_OPENFST_TYPE)
else:
    raise RuntimeError('implementation format not recognized')

transducers = []
istr = hfst.HfstInputStream()
while not istr.is_eof():
    transducers.append(istr.read())
istr.close()

if len(transducers) != 3:
    raise RuntimeError('Wrong number of transducers read.')

for i, re in enumerate(['föö:bär','0','0-0']):
    if not transducers[i].compare(hfst.regex(re)):
        raise RuntimeError('Transducers are not equivalent.')
if transducers:
    f = sys.stdout
    i=0
    transducers[i].write_att(f)
    i += 1
    while i < len(transducers):
        f.write('--\n')
        transducers[i].write_att(f)
        i += 1
