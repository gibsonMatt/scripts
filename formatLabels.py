input1 = open("labels.txt", "rU")
txt = ""
inpu = input1.read().spit()
for lab in inpu:
	txt = txt + "\"" + lab + "\"" + ", "

print txt
