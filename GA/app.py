import sys
import argparse
from xmlparser import XmlParser
from GA import GenAlg


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument ('file', nargs='?', default='new1.xml')
    arg_parser.add_argument ('output', nargs='?', default='output.jpg')
    args=arg_parser.parse_args()
    print (args.file)
    xparser=XmlParser(args.file)
    print (args.file)
    genalg=GenAlg(xparser.MUs, xparser.Terminals, xparser.Switchs, xparser.Logical_conns)
    drow=Drow(genalg.bestOsob, xparser.Logical_conns,xparser.MUs, xparser.Terminals, xparser.Switchs) 
    
    
