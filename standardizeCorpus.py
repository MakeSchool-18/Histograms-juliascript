import sys
from histogram import Histogram

def generateHistogramFromFile(filename):
	# returns sorted histogram of corpus
	histogram = Histogram()
	histogram = histogram.generateHistogramFromFile(filename)
	return histogram

if __name__ == "__main__":
	filename = sys.argv[1]
	generateHistogramFromFile(filename)