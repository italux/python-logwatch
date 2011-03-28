#!/usr/bin/python2.6

import os, sys
from optparse import OptionParser

def main():
    usage = "%prog [options] args"
    parser = OptionParser(usage)
    parser.add_option("-l", "--logfile", dest="logfile", help="Logfile to read data")
    parser.add_option("-p", "--logpos", dest="logpos", help="File to store last log line read position")
    parser.add_option("-f", "--find", dest="findstring", help="String to find in Logfile")
    (options, args) = parser.parse_args()
    if options.logfile is None or options.findstring is None or options.logpos is None:
        print("Incorrect arguments numbers.\n")
        parser.print_help()
        sys.exit(-1)
    else:
        logfile = options.logfile
        tofind = options.findstring
        logpos = options.logpos

        pos = 0
        count = 0
        if os.path.isfile(logpos):
            pos = int(open(logpos).readline() or 0)
        file = open(logfile)
        file.seek(pos)
        for line in file:
            if line.find(tofind) != -1:
                count += 1
        pos = file.tell()
        file.close()
        file = open(logpos, 'w')
        file.write(str(pos))
        file.close()
        print count

if __name__ == '__main__':

    main()
