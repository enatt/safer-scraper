# Setup
from PIL import Image
import pytesseract
import re
import pandas as pd
import numpy as np
from license_names import license_dict
from file_reader import file_parser

pytesseract.pytesseract.tesseract_cmd = r"tesseract.exe"

# Global variables used
cotd_count = 0
measures = [
    "Total Number of Applicants",
    "Number of Applicants with a Conviction",
    "Number of Licenses Granted",
    "Applicants with a Conviction Granted a License",
    "Number of Applicants Denied Licensure",
    "Number of Applicants Denied Licensure Because of Conviction",
    "Number of Applicants Granted a License on Probation",
    "Number of Licenses Granted an Expungement",
]
# NOTE: swapping_dict helps with replacing commonly misidentified characters
# Can edit as new common mistakes are found
swapping_dict = {
    "e)": "5",
    "c |": "3",
    "Zo": "29",
    "i)": "0",
    "pi": "2",
    "af": "27",
    "Z": "2",
    "a2": "22",
    "Fe": "73",
    "ae": "22",
    "eal": "51",
    "52]": "527",
    "a5": "35",
    "5S2": "582",
    "b)": "3",
    "=)": "5",
    "010": "0/0",
    "2}": "27",
}

# Loading in file names through helper
# NOTE: If running on different folder, change the argument of this function
file_names = file_parser("./safer2023")


### Helper functions
def parse_license_names(license_names):
    """
    Helper function for handling cases in which an Act psans multiple pages

    Args:
        license_names: a list (list of lists in the case of multi-page act)
        of licenses governed by a particular act

    Returns:
        A list of the license names on the given page
    """
    # If dealing with a list of list, cotd_count keeps track of how many
    # pages of the same act we've seen, returns proper page
    global cotd_count
    if type(license_names[0]) is list:
        act_length = len(license_names)
        license_names = license_names[cotd_count]
        cotd_count += 1
        if cotd_count == (act_length):
            cotd_count = 0

    return license_names


def parse_number_lines(all_lines):
    """

    Helper function to take all of the lines from the page, and extract the
    lines with numbers in them

    Args:
        all_lines (list): list of strings representing individual lines on
        the page

    Returns: list of individual lines, cleaned & filtered to only include the lines
            representing license statistics
    """
    # Extracting every line with numbers
    line_numbers = [x for x in all_lines if re.search(r"\d", x)]
    line_numbers = [x for x in line_numbers if "Act" not in x]

    # Replacing commonly misidentified characters
    for incorrect_k, real_v in swapping_dict.items():
        line_numbers = [line.replace(incorrect_k, real_v) for line in line_numbers]

    # Filtering to take only the numbers from the page (no page nums)
    line_numbers = line_numbers[:8]
    return line_numbers


# Iterate through each page, concatenate results
outputs = []
for f in file_names:
    print("Now reading", f)
    ocr_text = pytesseract.image_to_string(f, config="--psm 1", lang="eng")

    # Splitting PDF into lines
    lines = ocr_text.splitlines()

    # Using pre-defined dictionary to extract license names
    act_name = lines[0]
    l_names = license_dict[act_name]
    l_names = parse_license_names(l_names)

    # Getting lines with numbers, turn into pandas df
    line_numbers = parse_number_lines(lines)
    export_pd = pd.DataFrame(columns=["Measure"] + l_names)

    # For each line with numbers, assign to license
    for i, row in enumerate(line_numbers):
        # Add a check for page number
        if row.isdigit():
            continue
        # Try to set numbers as rows
        measure_name = [measures[i]]
        row_broken_up = re.split(r"^\D*", row)
        nums = row_broken_up[1].split(" ")
        try:
            export_pd.loc[i] = measure_name + nums
        except Exception:
            print("Issue with reading numbers in file", f)

    # Turn result into pandas dataframe, add to list of dataframes
    export_pd.set_index("Measure", inplace=True)
    outputs.append(export_pd)

# Concatenate results into one large dataframe, clean, export
final_pd = pd.concat(outputs, axis=1)
# Anything that's a letter in final columns, replace with NA
final_pd = final_pd.replace(to_replace=r"^[a-zA-Z]+$", value=np.nan, regex=True)
final_pd = final_pd.transpose()
final_pd.to_csv("scraped_table.csv")

# Printing
print(final_pd)
