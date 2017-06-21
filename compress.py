from bitarray import bitarray
import array
import itertools

def compare(index1, index2):
	while(fileContent[index1] == fileContent[index2]):
		index1=(index1+1)%fileContent.length()
		index2=(index2+1)%fileContent.length()
	return fileContent[index1]-fileContent[index2]

def lcp(index1,index2):
	lcp=0
	while(fileContent[index1] == fileContent[index2]):
		lcp=lcp+1
		index1=(index1+1)%fileContent.length()
		index2=(index2+1)%fileContent.length()
	return lcp

def scompute(index,stack):
	while(stack!=[] and LCP[index] <= LCP[stack[-1]]):
		stack.pop()
	if(stack==[]):
		stack.append(index)
		return 0
	else:
		retval = stack[-1]
		stack.append(index)
		return retval

def ecompute(index,stack,maxlen):
	while(stack!=[] and LCP[index] <= LCP[stack[-1]]):
		stack.pop()
	if(stack==[]):
		stack.append(index)
		return maxlen -1
	else:
		retval = stack[-1] -1
		stack.append(index)
		return retval



fileContent = bitarray('00110101') #bitarray()
##with open('lorem.txt', mode='rb') as file:
##	fileContent.fromfile(file)

indices = array.array('I',(i for i in range(0, fileContent.length())))
indices = sorted(indices,compare)

LCP = array.array('I',(itertools.chain([0],(lcp(f,s) for f,s in itertools.izip(indices, indices	 [1:])))))

stack = []
S = array.array('I',(scompute(i,stack) for i in range(0,fileContent.length())))

stack = []
maxlen = fileContent.length()
E = array.array('I', (0 for i in range(0, fileContent.length())))
for i in reversed(range(1,fileContent.length())):
	E[i] = ecompute(i,stack,maxlen) 

