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


def mintreeheight(data, lcp):
	lcp_max = 0
	no_of_sus = array.array('i',(0 for i in range(0,data.length()+1)))
	no_of_lcp = array.array('i',(0 for i in range(0,data.length())))
	for i in range(0,data.length()-1):
		if(lcp[i] >= 0):
			no_of_lcp[lcp[i]] += 1
		no_of_sus[1 + max(lcp[i],lcp[i+1] )] +=1
		lcp_max = max(lcp_max, lcp[i])
	print no_of_lcp
	print no_of_sus
	for i in range(0, lcp_max+1):
		if( (no_of_lcp[i] == 1 and no_of_sus[i+1]>=1) or no_of_lcp==0 ):
			return i+1
	return -1

fileContent = bitarray('00110101') #bitarray()
##with open('lorem.txt', mode='rb') as file:
##	fileContent.fromfile(file)

indices = array.array('i',(i for i in range(0, fileContent.length())))
indices = sorted(indices,compare)

LCP = array.array('i',(itertools.chain([-1],(lcp(f,s) for f,s in itertools.izip(indices, indices[1:])))))



stack = []
S = array.array('i',(scompute(i,stack) for i in range(0,fileContent.length())))

stack = []
maxlen = fileContent.length()
E = array.array('i', (0 for i in range(0, fileContent.length())))
for i in reversed(range(1,fileContent.length())):
	E[i] = ecompute(i,stack,maxlen) 

R = array.array('i', (0 for i in range(0, fileContent.length())))
zeros = 0
for i in range(0, fileContent.length()):
	zeros = zeros + 1 - fileContent[indices[i]-1]
	R[i] = zeros
