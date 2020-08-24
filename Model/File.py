import csv
import sys


class File:

	def __init__(self, fileInput = None):
		self.fileInput = fileInput
		self.dataInput = []

	def openFile(self, file, opening):
		return open(file, opening)

	
	def readFile(self):

		dataList = []

		with self.openFile(self.fileInput, "r") as csvFile:
			reader = csv.reader(csvFile)
			try:
				for line in reader:
					dataList.append(line)
			except csv.Error as e:
				sys.exit('csvFile %s, line %d: %s' % (self.fileInput, reader.line_num, e))

		csvFile.close()
		self.dataInput = dataList

	
	def readInput(self):
		self.readFile()


	def writeFile(self, origin, destiny, amount):
		print(origin + ',' + destiny + ',' + str(amount))
		try:
			
			newRoute = origin + ',' + destiny + ',' + str(amount)
			with open(self.fileInput, 'a+') as csvFile:
				csvFile.write('\n')
				csvFile.write(newRoute)
				csvFile.close()

			return True
		except: 
			print()
			return False