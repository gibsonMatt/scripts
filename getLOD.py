import sys

file1 = open(sys.argv[1], "r")

data = file1.read().split("\r")
print sys.argv[1]
prevGroup = 1
for line in data:
	l = line.split("\t")
	l.pop(0)
	if l[0] == "Group":
		continue
	if l[0] != "GW":

		group = int(l[0])
	
		if group == prevGroup:
			if float(l[5]) >= 0.95:
				print "Interval for group " + l[0] + ": " + l[1]
				prevGroup = prevGroup +1
			else:
				continue
		else:
			continue	
			
	else:
		group = "GW"
		if float(l[5]) >= .95:
			print "Interval for group " + group + ": " + l[1]
			break
		else:
			continue









file1.close()
