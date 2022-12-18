
path = r"C:\\Agromais\\CGD_AgroSanfona_20211201_20221214.xls"

# Import package.
import xlrd

# Load Excel file.
workbook = xlrd.open_workbook(path)

# List all sheet names.
print(workbook.sheet_names())

# Select sheet.
worksheet = workbook.sheet_by_index(0)

# Print value of cell.
print(worksheet.cell_value(rowx=0, colx=2))

# Print sheet stats.
print("{0} sheet has {1} rows and {2} columns".format(worksheet.name,
                                                      worksheet.nrows,
                                                      worksheet.ncols))