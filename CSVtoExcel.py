from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
import csv

# Importing an existing workbook
workbook = load_workbook("name_of_workbook.xlsx")
headers = 0
# Making reference to the sheet
worksheet = workbook.active
csv_file_path = "name_of_CSVfile.csv"


#Using the with statement to read the CSV file
with open(csv_file_path, 'r') as csv_file:
    CSVreader = csv.reader(csv_file)

    for rows in CSVreader:
        worksheet.append(rows)

# Turning the headers bold
for row in worksheet['A1:D1']:
    for cell in row:
        cell.font = Font(bold=True)


workbook.save("name_of_workbook.xlsx")
