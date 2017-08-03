# Short Google autoconplete scraper written in Python 2.

Takes an input text file and scrapes autocomplete suggestions for every line in that file.

Usage:
`python scraper.py INFILE_NAME MODE`

`INFILE_NAME` is the name of the input file 
`MODE` 0 to overwrite `INFILE_NAME` with suggestions, 1 to create new file and write the suggestions there.