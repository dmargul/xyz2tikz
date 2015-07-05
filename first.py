import csv
natoms = 1536
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
	"\ begin{document}"
	"\n"
	"\ begin{tikzpicture}"
	)
xyzstuff = []
for row in xyzrows:
	split_xyzrow = row.split(" , ")
	xyzstuff.append(split_xyzrow)

i = 1

for row in xyzstuff:
	try:
			row[1]
	except IndexError:
    		break
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
		outfile.write(row[3])
		outfile.write(",")
		outfile.write(row[4])
		outfile.write(
			")"
			"coordinate(O)" 
			"circle [radius=.73cm] ;"
			"\n"
				)
	if row[1] == 'H':
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=gray!100," 
			"right color=white!100!,"
			"shading angle=45]"
			"("
			)
		outfile.write(row[2])
		outfile.write(",")
		outfile.write(row[3])
		outfile.write(",")
		outfile.write(row[4])
		outfile.write(
			")"
			"coordinate(O)" 
			"circle [radius=.37cm] ;"
			"\n"
			)
	i = i + 1
outfile.write(
	"\end{tikzpicture}"
	"\n"
	"\end{document}"
	)