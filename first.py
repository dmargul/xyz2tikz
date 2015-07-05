import csv


C_options = ['C','CA','CB','CAT','CAY','CY']
H_options = ['H','HN','HB1','HB2','HB3','HT1',
			  'HT2','HT3','HNT','HY1','HY2','HY3']
O_options = ['O','OT','OY']
N_options = ['N','NT']

outfile = open('tikz_out.tex','w')
outfile.write(
	"\documentclass[tightpage]{standalone}"
	"\n"
	"\usepackage{varwidth}"
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

xyzfile = open('wxyz.csv','r')
xyzdata = xyzfile.read()
xyzrows = xyzdata.split('\n')
xyzstuff = []
for row in xyzrows:
	split_xyzrow = row.split(" , ")
	xyzstuff.append(split_xyzrow)


for row in xyzstuff:
	try:
			row[1]
	except IndexError:
    		break
	if row[1] in O_options:
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
	if row[1] in H_options:
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
			"coordinate(H)" 
			"circle [radius=.37cm] ;"
			"\n"
			)
	if row[1] in C_options:
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=black!100," 
			"right color=gray!100!,"
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
			"coordinate(H)" 
			"circle [radius=.77cm] ;"
			"\n"
			)
	if row[1] in N_options:
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=blue!100," 
			"right color=blue!70!,"
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
			"coordinate(H)" 
			"circle [radius=.75cm] ;"
			"\n"
			)						
outfile.write(
	"\end{tikzpicture}"
	"\n"
	"\end{document}"
	)