import csv
csvfliename = 'Patientsrxnt.csv'
csvfile = open(csvfliename, 'r', newline='')
csvreader = csv.reader(csvfile)
newcsvfilename = csvfliename.split('.')[0]+'_processed.csv'
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
	# print(newrow)

