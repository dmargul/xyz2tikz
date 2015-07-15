import csv
import numpy as np 
from operator import itemgetter

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
	"\usepackage{ifthen}"
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
	"\n"
	)

xyzfile = open('wxyz.csv','r')
xyzdata = xyzfile.read()
xyzrows = xyzdata.split('\n')
xyzstuff = []
for row in xyzrows:
	split_xyzrow = row.split(" , ")
	xyzstuff.append(split_xyzrow)

xyzstuff.remove([''])

for row in xyzstuff:
	row[4] = float(row[4])

xyzout = sorted(xyzstuff, key=(itemgetter(4)))
#print xyzout
#
#
#xyzout.remove(['', '', '', '', ''])
# un-comment if you awk'd a PDB into faux-XYZ
#
#

depth_shade = []
max_closeness = -1000
min_closeness = 1000
for row in xyzout:
	if (row[4]) > max_closeness:
		max_closeness = (row[4])
	if (row[4]) < min_closeness:
		min_closeness = (row[4])


closeness_range = max_closeness - min_closeness

for row in xyzout:
	depth_shade.append(((row[4]) - min_closeness)/closeness_range)


row_count = 0
for row in xyzout:
	if row[1] in O_options:
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=red!")
		outfile.write(str(round(100*depth_shade[row_count])))
		outfile.write(
			"!," 
			"right color=black!")
		outfile.write(str(round(30*depth_shade[row_count])))
		outfile.write(
			"!,"
			"shading angle=45]"
			"("
			)
		outfile.write(row[2])
		outfile.write(",")
		outfile.write(row[3])
		outfile.write(
			")"
#			"coordinate(O)" 
			"circle [radius=.73cm] ;"
			"\n"
				)
	elif row[1] in H_options:
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=gray!")
		outfile.write(str(round(100*depth_shade[row_count])))
		outfile.write(
			"!," 
			"right color=white!")
		outfile.write(str(round(100*depth_shade[row_count])))
		outfile.write(
			"!,"
			"shading angle=45]"
			"("
			)
		outfile.write(row[2])
		outfile.write(",")
		outfile.write(row[3])
		outfile.write(
			")"
#			"coordinate(H)" 
			"circle [radius=.37cm] ;"
			"\n"
			)
	elif row[1] in C_options:
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=black!")
		outfile.write(str(round(100*depth_shade[row_count])))
		outfile.write(
			"!," 
			"right color=gray!")
		outfile.write(str(round(100*depth_shade[row_count])))
		outfile.write(
			"!,"
			"shading angle=45]"
			"("
			)
		outfile.write(row[2])
		outfile.write(",")
		outfile.write(row[3])
		outfile.write(
			")"
#			"coordinate(C)" 
			"circle [radius=.77cm] ;"
			"\n"
			)
	elif row[1] in N_options:
		outfile.write(
			"\draw[black,thick," 
			"shading = axis,circle," 
			"left color=blue!")
		outfile.write(str(round(100*depth_shade[row_count])))
		outfile.write(
			"!," 
			"right color=blue!")
		outfile.write(str(round(70*depth_shade[row_count])))
		outfile.write(
			"!,"
			"shading angle=45]"
			"("
			)
		outfile.write(row[2])
		outfile.write(",")
		outfile.write(row[3])
		outfile.write(
			")"
#			"coordinate(N)" 
			"circle [radius=.75cm] ;"
			"\n"
			)	
	row_count = row_count + 1					
outfile.write(
	"\end{tikzpicture}"
	"\n"
	"\end{document}"
	)