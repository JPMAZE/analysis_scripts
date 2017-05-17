import argparse
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("output", nargs = "?")
args = parser.parse_args()

if not args.output:
	args.output = os.path.splitext(os.path.basename(args.file))[0] + ".png"

file = open(args.file.rstrip(),"r")

array_data = file.readlines()
number_columns = len(array_data[0].split("\t"))
array_columns = []

for i in range(number_columns):
	array_columns.append([])

for line in array_data[1:]:
	splitted_line = line.split("\t")
	for j in range(number_columns):
		array_columns[j].append(float(splitted_line[j].rstrip()))

file.close()

plt.plot(array_columns[0],array_columns[1], "gx")
plt.savefig(args.output.rstrip())