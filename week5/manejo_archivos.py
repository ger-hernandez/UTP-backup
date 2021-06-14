import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

#print(data)

#creating a dataframe to  use it for cvs conversion and excel
datosDataFrame = pd.DataFrame(data)

#print(datosDataFrame)

#turning the dataframe into an csv file and reading
datosDataFrame.to_csv('example.csv')
df = pd.read_csv('example.csv')

#turning the dataframe into an excel file and reading
datosDataFrame.to_excel('example_ex.xlsx', sheet_name='prueba')
df_ex = pd.read_excel('example_ex.xlsx', sheet_name='prueba' )

#print(df)
