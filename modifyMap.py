#Replaces Hs and blank cells with an X. DOESNT DO LAST COLUMN

input1 = open("1589.csv", "rU")
out1 = open("1589_hsmissing.csv", "w")

for line in input1:
	tmp = []
	for char in line.split(","):
		if len(char) < 1:
			print "HE"
		if char == 'H':
			tmp.append("X"+",")
		elif len(char) < 1:
			tmp.append("X"+",")
			print "HI"
		else:
			tmp.append(char+",")
	out1.write("".join(tmp))



input1.close()
out1.close()