#Extract consensus map from LPMerge output
files = []
names = []
out1 = open("consensusMap_full_2_2012.csv", "w")
for i in range(1, 13):
	names.append("consensusMap_" + str(i))
for x in range(1,13):
	f = open(names[x-1], "r")
	
	files.append(f)
print len(files)
chromo = 1
markers = []
chromosomes = []
positions = []
for file in files:
	for pp, line in enumerate(file):
		l = line.split()
		print l
		if pp == 0:
			pass
		else:
			markers.append(l[1])
			chromosomes.append(chromo)
			positions.append(l[2])
	chromo += 1

for i, marker in enumerate(markers):
	if marker[0:5] == "solcap":
		out1.write("sc" + marker[14:] + ",")
	else:
		out1.write(marker + ",")
out1.write("\n")
for i, c in enumerate(chromosomes):
	out1.write(str(c) + ",")
out1.write("\n")
for i, pos in enumerate(positions):
	out1.write(str(pos) + ",")
out1.write("\n")







out1.close()
for fi in files:
	fi.close()