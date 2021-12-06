import hfst
import hfst_commandline

impl=hfst.ImplementationType.TROPICAL_OPENFST_TYPE
skip_next = False
harmonize=True
semicolons=False
transducers_written=0

short_opts = 'f:HS'
long_opts = ['format=','do-not-harmonize','semicolon']
options = hfst_commandline.hfst_getopt(short_opts, long_opts, 1)
for opt in options[0]:
    if opt[0] in ['-f', '--format']:
        impl = hfst_commandline.get_implementation_type(opt[1])
    elif opt[0] in ['-H', '--do-not-harmonize']:
        harmonize= False
    elif opt[0] in ['-S', '--semicolon']:
        semicolons = True
istr = hfst_commandline.get_one_text_input_stream(options)[0]
ostr = hfst_commandline.get_one_hfst_output_stream(options, impl)[0]

comp = hfst.XreCompiler(impl)
comp.set_harmonization(harmonize)
if (semicolons):
    data = istr.read()
    i=0
    while (i < len(data)):
        tr_and_chars_read = comp.compile_first(data[i:]) # HFST 4.0: document this
        tr = tr_and_chars_read[0]
        i += tr_and_chars_read[1]
        if tr is None:
            if not comp.contained_only_comments():
                import sys
                sys.exit(1)
                raise RuntimeError('error in regexp compilation')
        else:
            ostr.write(tr)
            transducers_written += 1
else:
    for line in istr:
        tr = comp.compile(line)
        if tr != None:
            ostr.write(tr)
            transducers_written += 1
        elif not comp.contained_only_comments():
            import sys
            sys.exit(1)
            raise RuntimeError('error in regexp compilation')

ostr.close()
from sys import stdin
if istr != stdin:
    istr.close()

if transducers_written == 0:
    import sys
    sys.exit(1)
    raise RuntimeError('no transducer was written')
