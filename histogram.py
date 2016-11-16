import sys, operator, random, re

class Histogram:

	def __init__(self):
		self.dictionary = {}
		self._list = []

	def generateHistogramFromFile(self, textfile):
		# open text file 
		f = open(textfile, 'r')
		# read the file
		fileContent = f.read()
		cleanedFileContent = re.sub("[^a-zA-z' -]", "", fileContent).replace("_", " ")
		# generate array from file content
		wordsArray = cleanedFileContent.strip().replace('\n', ' ').split(' ')
		# generate histogram from words array
		histogram = {}
		for word in wordsArray:
			if word in histogram:
				histogram[word] = histogram[word] + 1
			else:
				histogram[word] = 1
		self.dictionary = histogram
		_list = sorted(histogram.items(), key=operator.itemgetter(1))
		# the most common word is '', so remove that
		self._list = _list[:-1]
		return self

	def leastFrequentWord(self):
		return self._list[0][0]

	def mostFrequentWord(self):
		return self._list[-1][0]

	def randomWord(self):
		return random.choice(self)

	def numberOfUniqueWords(self):
		return len(self)

	def averageFrequencyOfWords(self):
		numberOfWords = len(self)
		sumOfFrequencies = 0
		for word, frequency in self:
			sumOfFrequencies += frequency
		return sumOfFrequencies / numberOfWords

	def writeToFileWithName(self, filename):
		f = open(filename, 'w')
		for word, count in self:
			f.write("%s %i\n" % (word, count))




# def generateHistogramFromFile(textfile):
# 	# open text file 
# 	f = open(textfile, 'r')

# 	# read the file
# 	fileContent = f.read()

# 	# fileContent = fileContent.encode('utf-8', 'ignore')

# 	# generate array from file content
# 	wordsArray = fileContent.strip().replace('\n', ' ').split(' ')

# 	# generate histogram from words array
# 	histogram = {}
# 	for word in wordsArray:
# 		if word in histogram:
# 			histogram[word] = histogram[word] + 1
# 		else:
# 			histogram[word] = 1

# 	# function called zip --> tuple
# 	# hash function used to implement dictionaries
	
# 	return histogram

# def sortHistogram(histogram):
# 	return sorted(histogram.items(), key=operator.itemgetter(1))

# def leastFrequentWordIn(histogram):
# 	return histogram[0]

# def mostFrequentWordIn(histogram):
# 	return histogram[-1]

# def numberOfUniqueWordsIn(histogram):
# 	return len(histogram)

# def averageFrequencyOfWordsIn(histogram):
# 	numberOfWords = len(histogram)
# 	sumOfFrequencies = 0
# 	for word, frequency in histogram:
# 		sumOfFrequencies += frequency

# 	return sumOfFrequencies / numberOfWords

# def createHistogramFileWithName(filename, histogram):
# 	f = open(filename, 'w')
# 	for word, count in histogram:
# 		f.write("%s %i\n" % (word, count))

#-----
# def createWeightedListFromHistogram(histogram):
# 	_list = []
# 	for word, count in histogram:
# 		for i in range(count):
# 			_list.append(word)
# 	return _list
#-----

# def returnOneWordFromWeightedList(_list):
# 	return random.choice(_list)

if __name__ == "__main__":
	textFile = sys.argv[1]
	histogram = generateHistogramFromFile(textFile)
	sortedHistogram = sortHistogram(histogram)
	sortedHistogram = sortedHistogram[0:-1]
	# createHistogramFileWithName('histogram.txt', sortedHistogram)
	weightedList = createWeightedListFromHistogram(sortedHistogram)
	sentence = []
	for i in range(10):
		sentence.append(returnOneWordFromWeightedList(weightedList))	
	print sentence


