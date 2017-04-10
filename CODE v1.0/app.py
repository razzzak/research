import sys
import argparse
from xmlparser import XmlParser
from GA import GenAlg

defaultfilename="filename"

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument ('filename', nargs='?', default='file.xml')
    arg_parser.add_argument ('output', nargs='?', default='output.jpg')
    args=arg_parser.parse_args(sys.argv)
    xparser=XmlParser(args.filename)
    genalg=GenAlg(xparser.MUs, xparser.Terminals, xparser.Switchs, xparser.Logical_conns)
    drow=Drow(genalg.bestOsob, xparser.Logical_conns)
    
    
