import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
temperature = np.random.uniform(5, 35, size=365)
humidity = np.random.uniform(30, 90, size=365)
wind_speed = np.random.uniform(0, 20, size=365)

df = pd.DataFrame({
    'Data': dates,
    'Temperatura': temperature,
    'Umiditate': humidity,
    'Viteza Vantului': wind_speed
})

df['Temperatura Resimtita'] = df['Temperatura'] - 0.7 * (df['Umiditate'] / 100)

max_day = df.loc[df['Temperatura Resimtita'].idxmax()]
min_day = df.loc[df['Temperatura Resimtita'].idxmin()]
print("Ziua cu cea mai mare temperatura resimtita:")
print(max_day)
print("\nZiua cu cea mai mica temperatura resimtita:")
print(min_day)

plt.figure(figsize=(12, 5))
plt.plot(df['Data'], df['Temperatura'], label='Temperatura', alpha=0.7)
plt.plot(df['Data'], df['Temperatura Resimtita'], label='Temperatura Resimtita', alpha=0.7)
plt.title('Temperatura si Temperatura Resimtita pe parcursul anului')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df['Luna'] = df['Data'].dt.month
monthly_avg = df.groupby('Luna')['Temperatura'].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar')
plt.title('Temperatura medie lunara')
plt.xlabel('Luna')
plt.ylabel('Temperatura medie (°C)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
