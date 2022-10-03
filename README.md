# elemental-composition
Classify the compounds into classes based on elemental composition

The spreadsheet should have data like following format with elements(carbon, hydrogen, oxygen, nitrogen, sulphur, phosphorous) and the number of atoms.

```
C	H	O	N	S	P
4	6	3	0	0	0
5	10	2	0	0	0
4	8	3	0	0	0
7	8	1	0	0	0
```

Usage:
```
$ python main.py -h
usage: main.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-w OUTPUTWORKSHEET]

Molecular characterization

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Input Excel file
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output Excel file
  -w OUTPUTWORKSHEET, --outputworksheet OUTPUTWORKSHEET
                        Output worksheet name
```

