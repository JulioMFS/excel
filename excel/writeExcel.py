import datetime

# Import package.
import xlwt
loc = r"C:\\Agromais\\"
# Create a workbook.
workbook = xlwt.Workbook()

# Create a worksheet.
worksheet = workbook.add_sheet('My Fruits Sheet')

# Write 'apple' in row=0, col=0.
worksheet.write(0, 0, 'apple')

# Write 2.99 in row=0, col=1.
worksheet.write(0, 1, 2.99)

worksheet.write(0, 2, 'banana')
worksheet.write(0, 3, 4.99)

# Add formula at row=1, col=1
worksheet.write(1, 1, xlwt.Formula("B1+D1"))

# Add datetime and format cell as 'D-MMM-YY'.
dt_style = xlwt.easyxf(num_format_str='D-MMM-YY')
worksheet.write(2, 0, datetime.datetime.now(), dt_style)

# Save the file
workbook.save("sample.xls")