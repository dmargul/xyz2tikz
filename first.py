import csv

xyzfile = open('wxyz.csv','r')
xyzdata = xyzfile.read()
xyzrows = xyzdata.split('\n')
outfile = open('tikz_out.tex','w')
outfile.write(
	"\documentclass{article}"
	"\n"
	"\usepackage[letterpaper,landscape]{geometry}"
	"\n"
	"\usepackage{tikz}"
	"\n"
	"\usepackage{tikz-3dplot}"
	"\n"
	"\usepackage{verbatim}"
	"\n"
	"\usetikzlibrary{arrows}"
	"\n"
	"\usepackage{fontspec}"
	"\n"
	"\begin{tikzpicture}"
	)
xyzstuff = []
for row in xyzrows:
	split_xyzrow = row.split(" , ")
	xyzstuff.append(split_xyzrow)

for row in xyzstuff:
	if row[1] == 'O':
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=red!100," 
			"right color=black!30!,"
			"shading angle=45]"
			"("
			)
		outfile.write(row[2])
		outfile.write(",")
		outfile.write("\n")