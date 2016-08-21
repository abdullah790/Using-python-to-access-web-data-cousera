import re
rf = open('act_data.txt','r')
numlist= list()
for line in rf:
	line = line.rstrip()
	x = re.findall('([0-9]+)',line)
	for i in x:
		numlist.append(int(i))
print sum(numlist)



