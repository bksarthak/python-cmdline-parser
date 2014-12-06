#This file has been created to try out a command line sorter, which prints the output to another file using Python.
import sys
def write_output(inputfile,outputfile):
  openFile = open(inputfile,'r')
  fileContent = openFile.read()
  lines = fileContent.lower()
  words = lines.split()
  sortedWords = sorted(words)
  writeFile = open(outputfile,'w')
  writeFile.write(sortedWords)
  openFile.close()
  writeFile.close()

def print_reverse(inputfile):
 
  
def main():
  if len(sys.argv)!=4:
    print 'Incorrect usage: Use like "./sort.py {-o|--output|-r|--reverse} inputFilename outputFilename"'
    sys.exit(1)
  
  flag = sys.argv[1]
  inputfile = sys.argv[2]
  outputfile = sys.argv[3]
  
  if (flag=='-o' or flag=='--output'):
    write_output(inputfile,outputfile)
  elif (flag=='-r' or flag=='--reverse'):
    print_reverse(inputfile)
  else:
    print('Error with option entered')
    sys.exit(1)
    
if __name__ == '__main__':
  main()
