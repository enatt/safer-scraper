# Setup
from PIL import Image
import pytesseract
import re
import pandas as pd
import numpy as np
from license_names import license_dict
from file_reader import file_parser
pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'
cotd_count = 0
# Loading in file names through helper
file_names = file_parser("./safer2023")

### Helper functions
def parse_license_names(license_names):
    global cotd_count
    if type(license_names[0]) is list:
        act_length = len(license_names)
        license_names = license_names[cotd_count]
        cotd_count += 1
        if cotd_count == (act_length):
            cotd_count = 0

    return license_names

def parse_number_lines(all_lines):
    # Extracting every line with numbers
    line_numbers = [x for x in all_lines if re.search(r'\d',x)]
    line_numbers = [x for x in line_numbers if "Act" not in x]

    # Replacing commonly misidentified characters
    line_numbers = [sub.replace("e)", "5") for sub in line_numbers]
    line_numbers = [sub.replace("c |", "3") for sub in line_numbers]
    line_numbers = [sub.replace("Zo", "29") for sub in line_numbers]
    line_numbers = [sub.replace("i)", "0") for sub in line_numbers]
    line_numbers = [sub.replace("pi", "2") for sub in line_numbers]
    line_numbers = [sub.replace("af", "27") for sub in line_numbers]
    line_numbers = [sub.replace("Z", "2") for sub in line_numbers]
    line_numbers = [sub.replace("a2", "22") for sub in line_numbers]
    line_numbers = [sub.replace("Fe", "73") for sub in line_numbers]
    line_numbers = [sub.replace("ae", "22") for sub in line_numbers]
    line_numbers = [sub.replace("eal", "51") for sub in line_numbers]
    line_numbers = [sub.replace("52]", "527") for sub in line_numbers]
    line_numbers = [sub.replace("a5", "35") for sub in line_numbers]
    line_numbers = [sub.replace("5S2", "582") for sub in line_numbers]
    line_numbers = [sub.replace("b)", "3") for sub in line_numbers]
    line_numbers = [sub.replace("=)", "5") for sub in line_numbers]

    # Filtering for no extra numbers at bottom of page
    line_numbers = line_numbers[:8]
    return line_numbers

#Adding for loop
outputs = []
for f in file_names:
    print("Now reading", f)
    ocr_text = pytesseract.image_to_string(f, config='--psm 1', lang='eng')

    # Splitting PDF into lines
    lines = ocr_text.splitlines()

    # Using pre-defined dictionary to extract license names
    act_name = lines[0]
    l_names = license_dict[act_name]

    l_names = parse_license_names(l_names)

    # Getting line numbers
    line_numbers = parse_number_lines(lines)
    # Once we have all the lines with numbers, we turn it into a pandas df
    export_pd = pd.DataFrame(columns=["Measure"]+l_names)
    measures = ["Total Number of Applicants", "Number of Applicants with a Conviction", "Number of Licenses Granted", "Applicants with a Conviction Granted a License", "Number of Applicants Denied Licensure",
                "Number of Applicants Denied Licensure Because of Conviction", "Number of Applicants Granted a License on Probation", "Number of Licenses Granted an Expungement"]

    for i, row in enumerate(line_numbers):
        # Add a check for page number
        if row.isdigit():
            continue
        measure_name = [measures[i]]
        row_broken_up = re.split(r"^\D*", row)
        nums = row_broken_up[1].split(" ")
        try:
            export_pd.loc[i] = measure_name + nums
        except Exception:
            print("Issue with reading numbers in file", f)

    export_pd.set_index('Measure', inplace=True)
    outputs.append(export_pd)

# Making some corrections, exporting to CSV
final_pd = pd.concat(outputs, axis=1)
final_pd = final_pd.replace(["i", "010", "2}"], [1, "0/0", 27])
final_pd = final_pd.replace(to_replace=r'^[a-zA-Z]+$', value=np.nan, regex=True)
final_pd = final_pd.transpose()
final_pd.to_csv("scraped_table.csv")

# Printing
print(final_pd)

### Helper functions
def parse_license_names(license_names):
    if type(license_names[0]) is list:
        act_length = len(license_names)
        license_names = license_names[cotd_count]
        cotd_count += 1
        if cotd_count == (act_length):
            cotd_count = 0

    return license_names