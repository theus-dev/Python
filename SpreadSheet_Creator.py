from openpyxl import Workbook
from openpyxl.styles import Font

# Create a new workbook (a workbook is created with at least one sheet by default)
workbook = Workbook() # Ao instanciar a classe Workbook, ela será criada com uma planilha, contendo ao menos uma sheet

# Access the default sheet created by the workbook
worksheet = workbook.active # acessando a planilha gerada por workbook
worksheet.title = "SmarthPhone Sales"


sales_data = [
    ["Name", "Price"],
    ["Iphone 13", 5999],
    ["Iphone 15 pro", 10999],
    ["iphone Xr", 2000]
]

# Populate the worksheet with sales data
for rows in sales_data:
    worksheet.append(rows)

for row in worksheet['A1:B1']:
    for cell in row:
        cell.font = Font(bold=True)


workbook.save("Sales spreadsheet.xlsx") # Save the workbook with a desired name
