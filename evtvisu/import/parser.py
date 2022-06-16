import pandas as pd

data = pd.read_excel (r'../data/energiedaten-gesamt-xls-2022.xlsx', sheet_name='6')
df = pd.DataFrame(data, columns= ['Energieträger','1991'])
print (df)