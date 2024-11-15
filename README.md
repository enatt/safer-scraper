## SAFER Scraper ##
This scraper is built to read information from the Illinois Department of Financial and Professional Regulation (IDFPR)'s annual SAFER reports. It is built using pytesseract in Python. 

## Setup ##
In order for the code in scraper.py to function, the following steps must be completed:
1. While the SAFER reports are usually distributed in .pdf format, the scraper must be run on images in .jpg format. 
Thus, the first necessary step prior to script execution is to convert the report from .pdf to .jpg format. It is recommended
to use [SmallPDF converter](https://smallpdf.com/pdf-to-jpg#r=convert-to-image).
2. pytesseract must be installed and accessible to this repository. See [pytesseract documentation](https://pypi.org/project/pytesseract/) for information on installation and path setup.

## Execution
The code can be ran from the terminal with the line ```python3 scraper.py```
