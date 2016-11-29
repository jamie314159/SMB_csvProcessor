import os
import csv
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

csvfliename = filedialog.askopenfilename(title="Open File to Process")
newcsvfilename = filedialog.asksaveasfilename(title="Save File As", defaultextension = ".csv")

if csvfliename and newcsvfilename:
	csvfile = open(csvfliename, 'r', newline='')
	csvreader = csv.reader(csvfile)
	newcsvfile = open(newcsvfilename, 'w',  newline='')
	csvwriter = csv.writer(newcsvfile, quoting=csv.QUOTE_MINIMAL)
	csvheader = ["LastName", "FirstName", "MiddleInitial"]
	for x in csvreader.__next__()[1:]:
		csvheader.append(x)
	csvwriter.writerow(csvheader)

	for row in csvreader:
		name = row[0].replace(',', '').split(' ')
		lName = name[0].upper()
		fName = name[1].upper()
		mName = (name[2].upper() if len(name) == 3 else '')
		newrow = [lName, fName, mName]
		[newrow.append(x) for x in row[1:]]
		csvwriter.writerow(newrow)

	csvfile.close()
	newcsvfile.close()
	os.startfile(newcsvfilename.replace('/','\\'))