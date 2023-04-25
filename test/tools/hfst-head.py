import hfst
import hfst_commandline
nfirst=None
infile=None

short_getopts='n:'
long_getopts=['n-first=']
options = hfst_commandline.hfst_getopt(short_getopts, long_getopts, 1)

for opt in options[0]:
    if opt[0] in ['-n', '--n-first']:
        nfirst = int(opt[1])
istr = hfst_commandline.get_one_hfst_input_stream(options)[0]
ostr = hfst.HfstOutputStream(type=istr.get_type())

if nfirst > 0:
    n=0
    for tr in istr:
        if n >= nfirst:
            break
        ostr.write(tr)
        n += 1
elif nfirst < 0:
    transducers = list(istr)
    for n, tr in enumerate(transducers):
        if n < (len(transducers) + nfirst):
            ostr.write(tr)
istr.close()
ostr.close()
