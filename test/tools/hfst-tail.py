import hfst
import hfst_commandline
nlast=None
from_nth=None
infile=None

short_getopts='n:'
long_getopts=['n-last=']
options = hfst_commandline.hfst_getopt(short_getopts, long_getopts, 1)

for opt in options[0]:
    if opt[0] in ['-n', '--n-last']:
        nlast = int(opt[1])
istr = hfst_commandline.get_one_hfst_input_stream(options)[0]
ostr = hfst.HfstOutputStream(type=istr.get_type())

if from_nth != None:
    for n, tr in enumerate(istr, start=1):
        if n >= from_nth:            
            ostr.write(tr)
elif nlast != None:
    transducers = list(istr)
    for i, tr in enumerate(transducers):
        if i >= len(transducers) - nlast:
            ostr.write(tr)
istr.close()
ostr.flush()
ostr.close()
