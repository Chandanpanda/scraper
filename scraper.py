import urllib, urllib2, json, sys

def main():
	if len(sys.argv) != 3:
		print 'Error: Incorrect number of arguments.\nUsage: python scraper.py INFILE MODE\n MODE: 0 to overwrite input file, 1 to write to new file' 
		sys.exit()

	try: 
		infile = open(sys.argv[1], 'r+w')
	except:
		print 'Error: provided file does not exist.'
		sys.exit()
	
	if sys.argv[2] == '0':
		lines = [line.rstrip('\n') for line in infile]
		infile.seek(0, 0)
		for line in lines:
			if line != '\n':
				url = 'http://suggestqueries.google.com/complete/search?client=firefox&q=' + urllib.quote(line)
				request = urllib2.Request(url)
				response = urllib2.urlopen(request)
				fills = json.loads(response.read())
				infile.write(fills[1][0] + '\n')
	elif sys.argv[2] == '1':
		outfile = open(suffixedName(sys.argv[1], 'autocompleted'), 'w+')
		for line in infile:
			if line != '\n':
				url = 'http://suggestqueries.google.com/complete/search?client=firefox&q=' + urllib.quote(line)
				request = urllib2.Request(url)
				response = urllib2.urlopen(request)
				fills = json.loads(response.read())
		outfile.close()
	else:
		print 'Error: invalid MODE provided.\n\nUsage: python scraper.py INFILE MODE\n MODE: 0 to overwrite input file, 1 to write to new file'

	infile.close()

""" Turns name.extension into namesuffix.extension """
def suffixedName(name, suffix):
	outname = ''
	for i in range(len(name)):
		if name[i] == '.':
			outname += suffix
			outname += '.'
		else:
			outname += name[i]
	return outname

if __name__ == "__main__":
	main()