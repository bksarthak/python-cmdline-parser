#This file has been created to try out a command line parser in Python.

def main():
  if len(sys.argv)!=3:
    print 'Incorrect usage: Use like "./sort.py {-o|--output|-r|--reverse} input filename {output filename}"'
    sys.exit(1)
  flag = sys.argv[1]
  inputfile = sys.argv[2]
  if (flag=='-o' or flag=='--output'):
    write_output(inputfile)
  elif (flag=='-r' or flag=='--reverse'):
    print_reverse(inputfile,outputfile)
  else:
    print('Error with option entered')
    sys.exit(1)
    
if _name_ == '_main_':
  main()
