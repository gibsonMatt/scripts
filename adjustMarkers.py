n1 = open("markers.csv", "r")
out1 = open("mout.csv", "w")
markers = n1.read().split(",")
newM = []
for m in markers:
	if m[0] == "*":
		newM.append(m[1:])
	else:
		newM.append(m)
for m in newM:
	out1.write(m + ",")

n1.close()
out1.close()
