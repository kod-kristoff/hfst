import hfst
import hfst_commandline

options = hfst_commandline.hfst_getopt('', [], 0)
istr = hfst_commandline.get_one_hfst_input_stream(options)[0]
for n, tr in enumerate(istr, start=1):
    ostr = hfst.HfstOutputStream(filename=str(n) + ".hfst", type=tr.get_type())
    ostr.write(tr)
    ostr.flush()
    ostr.close()
istr.close()
