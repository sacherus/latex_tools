#!/usr/bin/python2
import sys, getopt
from sys import argv

def parse(filename):
    start='{'

    if(start == '{'):
        end='}'
    s=[]
    i=1
    with open(filename) as f:
        for l in f:
            p=''
            for c in l:
                if c == '%':
                    break
                elif p == '\\':
                    next
                elif c == start:
                    s.append((c,i))
                elif c == end:
                    if len(s) == 0:
                        return (c,i)
                    else:
                        s.pop()
                p=c
            i+=1

    if len(s) > 0:
        return s

def main(script_name, argv):
    filename = ''
    usage_msg=(script_name + ' -i <inputfile.tex>', "eg. ./para_parser.py -i main_simple.tex", \
    "Input file is  main_simple.tex", "Found redundant parenthesis in ('}', 3)")
    usage_msg="\n".join(usage_msg)
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
       print usage_msg
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print usage_msg
          sys.exit()
       elif opt in ("-i"):
          filename = arg
    if not filename:
        print usage_msg
        sys.exit(2)
    
    print 'Input file is ', filename
    ret = parse(filename)
    if ret:
        print "Found redundant parenthesis in", ret
    else:
        print "Could not find redundant parenthesis" 

if __name__ == "__main__":
    main(argv[0], sys.argv[1:])



