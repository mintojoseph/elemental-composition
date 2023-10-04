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

Data output will be in a format which can be used to plot in a tool such as [Origin](https://en.wikipedia.org/wiki/Origin_(data_analysis_software)). 

Usage:
```
pip install -r requirements.txt

$ python elemental_composition.py -h
usage: main.py [-h] [-i INPUTFILE]

Molecular characterization

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Input Excel file
```

For Biochemical Classification

```
python biochemical_classification.py -h
usage: biochemical_classification.py [-h] [-i INPUTFILE]

Biochemical Classification

options:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Input Excel file
```                        