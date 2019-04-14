import quandl
import sys, getopt

def main(argv):
   key = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["key=","ofile="])
   except getopt.GetoptError:
      print 'test.py -k <key> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -k <key> -o <outputfile>'
         sys.exit()
      elif opt in ("-k", "--key"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   return key, outputfile

if __name__ == "__main__":
    key, outputfile = main(sys.argv[1:])
    data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = ['APC', 'BHVN', 'PCG','ADNT'], date = { 'gte': '2018-01-01', 'lte': '2019-04-12' }, api_key=key)
    data.write_csv("../../data"+outputfile)
