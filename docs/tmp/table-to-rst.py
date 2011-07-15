import argparse
import re
import xml.etree.cElementTree as etree


camelcase_to_underscore = lambda str: re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', str).lower().strip('_')

parser = argparse.ArgumentParser(description='Convert HTML tables to RST attribute lists.')
parser.add_argument('table', type=str, help="Filename of table to process")
args = parser.parse_args()

tree = etree.parse(open(args.table))

for tr in tree.findall("table/tbody/tr"):
    for i, td in enumerate(tr.findall("td")):

        string = td.text
        
        for i in td.getchildren():
            if i is not None: 
                string += i.text
                string += i.tail

        if i == 0:
            print "   .. attribute:: " + camelcase_to_underscore(string)
        else:
            print "      " + string

        print

            
            



