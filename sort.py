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
  openFile = open(inputfile,'r')
  fileContent = openFile.read()
  lines= fileContent.lower()
  words = lines.split()
  sortedWords = sorted(words,reverse=True)
  print sortedWords
  
def main():
  parser = argparse.ArgumentParser()
	parser.add_argument ('-o','--output',dest='filename',action='store',metavar='OUTPUTFILE', help='print output to file')
	parser.add_argument('-r','--reverse',dest='filename',action='store',metavar='INPUTFILE', help ='display reverse sorting')
	args = parser.parse_args()
	
	if sys.argv[]:
		write_output(sys.argv[-2],sys.argv[-1])
	elif args.reverse:
		print_reverse(sys.argv[-1])
	else:
	 print('something is wrong')
	  
if __name__ == '__main__':
  main()
