#Gets map (marker name, chr, and pos) from SolGenomics map file.

file = open("expimp_2012_map_TG", "r")
out1 = open("expimp_2012_map_tidy.csv", "w")
x = 0
#SGN id	marker	protocol	map	chromosome	position	confidence
for line in file:
	l = line.split()
	if x == 0:
		out1.write("marker"+ "," + "chr" + "," + "pos"+"\n")
	else:
		out1.write(l[1]+ "," + l[5] + "," + l[6]+"\n")
	x += 1

file.close()
out1.close()