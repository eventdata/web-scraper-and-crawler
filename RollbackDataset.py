import json
from StringIO import StringIO
import sys
import Util


reload(sys)
sys.setdefaultencoding('utf8')


input_file = open("/Users/sxs149331/Desktop/window_all.txt")
output_file = open("/Users/sxs149331/Desktop/window_all_sgml.txt", "w+")

for line in input_file:
    if line.startswith("#"):
        output_file.write(line) # writing window marker
    elif line.startswith("{"):
        doc = json.load(StringIO(line))
        sgml_line = Util.json_toSGML(doc)
        output_file.write(sgml_line+"\n")

output_file.close()
input_file.close()




