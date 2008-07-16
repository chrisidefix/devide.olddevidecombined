# NB: modify the following three variables!
# complete list of PA*.txt filenames you want to process
INPUT_FILENAMES = [
        'PA000000.txt', 
        'PA000001.txt'
        ]
# directory where the PA*.txt files are located
INPUT_DIR = 'C:\\work\\projects\\ruben-spine\\article_mri_spine'
# name of the output CSV file
OUTPUT_FILENAME = \
        'C:\\work\\projects\\ruben-spine\\article_mri_spine\output.csv'

import csv
import os
import re

# regular expressions to match the path lines
# use raw string, else we need four slashes
P_REPO = re.compile(r'^([A-Za-z]:\\.*$)')

# regular expressions to match the CORD and SAC ellipse lines
FRE = r'[-+]?[0-9]*\.?[0-9]+'
E_RE = 'c = \[(%s), (%s), 0\.0\], rv = \(\[(%s), (%s), 0\.0\], ' \
        '\[(%s), (%s), 0\.0\].*$' % tuple((FRE,) * 6)
CORD_REPO = re.compile('.*CORD ellipse.*%s' % E_RE)
SAC_REPO = re.compile('.*SAC ellipse.*%s' % E_RE)

TS_REPO = re.compile('^[0-9]+:.*$')

def parse_file(input_file, csvwriter):
    for line in input_file:
        # skip empty lines
        if not line.strip():
            continue

        mo = P_REPO.match(line)
        if mo:
            # new path means a new start
            # filename, space, 6 floats, space, 6 floats = 15
            output_line = [''] * 16 

            output_line[0] = mo.groups()[0]
            continue

        mo = CORD_REPO.match(line)
        if mo:
            output_line[2:8] = ['=%s' % (i,) for i in mo.groups()]
            continue

        mo = SAC_REPO.match(line)
        if mo:
            output_line[9:15] = ['=%s' % (i,) for i in mo.groups()]
            # we've found the SAC, so now we can write the complete
            # line
            csvwriter.writerow(output_line)

        # now it can only be a timestamped line, or a posture line 
        #if not TS_REPO.match(line):
        #    print line



def main():
    ofile = open(OUTPUT_FILENAME, 'wb')
    csvwriter = csv.writer(ofile)
    for ifname in INPUT_FILENAMES:
        ifile = open(os.path.join(INPUT_DIR, ifname), 'r')
        print "Parsing %s" % (ifname,)
        parse_file(ifile, csvwriter)
        ifile.close()

    ofile.close()


if __name__ == '__main__':
    main()

