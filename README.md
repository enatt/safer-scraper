## Info ##
This scraper is built to read information from the Illinois Department of Financial and Professional Regulation (IDFPR)'s annual SAFER reports. It is built using pytesseract in Python. 

## Setup ##
### Document Format ###
The SAFER reports are distributed in PDF format. For the scraper to function, it must be ran on images in .JPG format. Complete the following steps to prepare the images. 
1. Save a version of the SAFER report including only pages with information tables

   a. For example, take [the 2023 SAFER report](https://idfpr.illinois.gov/content/dam/soi/en/web/idfpr/forms/ar/May-2024-pa-100-0286.pdf)
   
   b. Click "print" and select "Save as PDF" under "Destination".

   c. Under "Pages", select "Custom", and enter the page numbers with tables on them -- for example, (6-77, 79-85)

   d. Save as PDF
   
2. Convert the PDF you made in (1) into a series of .JPG images. It is recommended that you use [SmallPDF converter](https://smallpdf.com/pdf-to-jpg#r=convert-to-image). SmallPDF will export a zip folder of a .JPG images.
3. Extract and copy the zip folder into the same directory as the scraper (here, the folder ``safer2023`` is an example of what the folder should look like)

You are complete with file setup. Move on to package management set up below.

### Package Management ###
The dependencies for this project are managed by ```uv```. 
1. Upon cloning this repository, move into the ```safer-scraper``` directory and run the command: ```uv sync```
2. One of the requirements for this project is the ```pytesseract``` package. See [pytesseract documentation](https://pypi.org/project/pytesseract/) for information on installation and path setup.

## Execution ##
The code can be ran from the terminal with the line ```python3 scraper.py``` from the ```safer-scraper``` directory. Upon script completion, a file called ```scraped_table.csv``` will populate in this repository including all of the scraped information.

## FAQs/Contact ##
#### I'm running into issues with pyteseract ####
Consult the [pytesseract documentation](https://pypi.org/project/pytesseract/), as well as the following resources on common pytesseract errors: 
- [Error when executing pytesseract to get the text from image](https://python-forum.io/thread-15111.html)
- [Unicode errors in pytesseract](https://github.com/madmaze/pytesseract/issues/26)

#### Some of the cells are blank in my scraped_table.csv, what happened? ####
Sometimes the scraper runs into a character it can't read. In such cases, it will return blanks/NAs. 

#### I'm getting "key errors" when trying to read license names ####
The file ```license_dict.py``` includes a dictionary mapping acts to the occupations they regulate. As regulated occupations change each year, the dictionary in ```license_dict.py``` must change as well. It is currently configured for the most recent SAFER report (2023). If running the scraper on other years, alter the dictionary accordingly (further instructions in ```license_dict.py```). 

#### Something isn't working! Help! ####
Feel free to submit an Issue on this GitHub page, or contact me at enattinger@uchicago.edu
