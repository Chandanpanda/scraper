# Short Google autocomplete scraper written in Python 2.

Inspired by [this image](https://i.redd.it/9dukhq4nwfdz.jpg), scraper.py takes an input text file and scrapes autocomplete suggestions for every line in that file.

Usage:
`python scraper.py INFILE_NAME MODE`

* `INFILE_NAME`: This is the name of the input file.
* `MODE` : 0 to overwrite `INFILE_NAME` with suggestions, 1 to create new file and write the suggestions there.

##Example 
Input:
> how\n
> why\n
> when\n
> where\n
> who\n

Output:
> how to make slime\n
> why him\n
> when is easter\n
> where am i\n
> who is the next bachelor\n