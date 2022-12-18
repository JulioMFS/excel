# with open('C:\\Users\\User\\Downloads\\CGD_11Nov2022.csv') as csvfile:
import csv
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["DataMov", "DataValor", "Descricao", "Montante", "Saldo"]

with open('C:\\Users\\User\\Downloads\\CGD_11Nov2022.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')

    for lines in csv_reader:
        line = " "
        i = 0
        while i < len(lines):
            line = line + lines[i]
            i += 1
 #       print(line)
        table.append_row([lines[0],lines[1],lines[2],lines[3],lines[4] ])
    print(table)


