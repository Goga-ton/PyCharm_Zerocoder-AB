import pandas as pd

df = pd.read_csv('youtube-top-100-songs-2025.csv')
print(df.head())
print(df.info())
print(df.describe())

df = pd.read_csv('dz.csv')
df['City'].fillna('Неизвестность', inplace=True)
df['Salary'].fillna(0, inplace=True)
sr = df['Salary'].mean()
print(f"Средняя З/п определнная по ост.З/п = {sr}")
df['Salary'].fillna(sr, inplace=True)
gr = df.groupby('City')['Salary'].mean()
print(gr)
