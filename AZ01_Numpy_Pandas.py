# Просмотр данных и запсиь в файл

import pandas as pd

data = [1, 2, 3, 4, 5]
ser = pd.Series(data)
print(ser)

data = {
     'Name': ['Alica', 'Bob', "Roma", 'Anna'],
     'Age': [20, 45, 18, 36],
     'City': [ 'Moscow', "Tambov", 'Kalyga', 'Rim']}
df = pd.DataFrame(data)
df.to_csv('animal-1.csv', index=False) #запись в файл
print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df[df['Healthy life expectancy'] > 0.7])
print(df[['Country name', 'Freedom to make life choices']])


# Работа с данными

import pandas as pd

df = pd.read_csv('hh.csv')

df['Test'] = [new for new in range(50)] # Добавляем столбец Test
print(df)

df.drop('Test', axis=1, inplace=True) #Удаляем столбец Test
print(df)

df.drop(48, axis=0, inplace=True) # Удаляем 49 строчку
print(df)


#замена отсутсвующей информации и удаление

import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

df.fillna(0, inplace=True)
print(df)

df.dropna(inplace=True)
print(df)


import pandas as pd

df = pd.read_csv('animal.csv')
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(df)
print(group)
