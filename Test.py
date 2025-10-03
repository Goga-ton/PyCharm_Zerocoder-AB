import pandas as pd

data = {
     'Name': ['Alica', 'Bob', "Roma", 'Anna'],
     'Age': [20, 45, 18, 36],
     'City': [ 'Moscow', "Tambov", 'Kalyga', 'Rim']}
df = pd.DataFrame(data)

df.to_csv('animal-1.csv', index=False)

