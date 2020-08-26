import csv
import sys


class File:

	def __init__(self, fileInput = None):
		self.fileInput = fileInput
		self.dataInput = []

	def isBlank (self, data):
		if data and data.strip():
			return False
		
		return True

	def openFile(self, file, openning):
		return open(file, openning)

	
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
		
		if self.isBlank(origin):
			return False
		elif self.isBlank(destiny):
			return False
		elif amount <= 0:
			return False

		try:
			
			newRoute = origin + ',' + destiny + ',' + str(amount)
			with open(self.fileInput, 'a+') as csvFile:
				csvFile.write('\n')
				csvFile.write(newRoute)
				csvFile.close()

			return True
		except: 
			return False

	