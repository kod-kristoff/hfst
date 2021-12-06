import hfst
import hfst_commandline

shortopts = 'n'
longopts = ['newline']
options = hfst_commandline.hfst_getopt(shortopts, longopts, 1)
newline = any(opt[0] in ['-n', '--newline'] for opt in options[0])
#    raise RuntimeError('Usage: hfst-pmatch.py [--newline] INFILE')
istr = hfst_commandline.get_one_hfst_input_stream(options)[0]

transducers = list(istr)
istr.close()
cont = hfst.PmatchContainer(transducers)

from sys import stdin
if newline:
    for line in stdin:
        print(cont.match(line), end='')
else:
    exp=''
    for line in stdin:
        exp += line
        if line == '':
            print(cont.match(line), end='')
    if line != '':
        print(cont.match(line), end='')
