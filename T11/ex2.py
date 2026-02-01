import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
days = 730
dates = pd.date_range(start='2023-01-01', periods=days, freq='D')
daily_changes = np.random.normal(0, 0.02, size=days)

closing_prices = np.zeros(days)
closing_prices[0] = 100
for i in range(1, days):
    closing_prices[i] = closing_prices[i - 1] * (1 + daily_changes[i])

df = pd.DataFrame({
    'Data': dates,
    'Schimbare Zilnica (%)': daily_changes * 100,
    'Pret de Inchidere': closing_prices
})

df['Media Mobila 30'] = df['Pret de Inchidere'].rolling(window=30).mean()
df['Media Mobila 100'] = df['Pret de Inchidere'].rolling(window=100).mean()

df['Peste Media 100'] = df['Pret de Inchidere'] > df['Media Mobila 100']

print("Perioade in care pretul a fost peste media mobila de 100 de zile:")
above = df[df['Peste Media 100']].copy()
above['Group'] = (above['Peste Media 100'] != above['Peste Media 100'].shift()).cumsum()
for _, group in above.groupby('Group'):
    print(f"  {group['Data'].iloc[0].date()} - {group['Data'].iloc[-1].date()}")

plt.figure(figsize=(14, 6))
plt.plot(df['Data'], df['Pret de Inchidere'], label='Pret de Inchidere', alpha=0.8)
plt.plot(df['Data'], df['Media Mobila 30'], label='Media Mobila 30 zile', alpha=0.8)
plt.plot(df['Data'], df['Media Mobila 100'], label='Media Mobila 100 zile', alpha=0.8)

above_mask = df['Peste Media 100'].values
plt.fill_between(df['Data'], df['Pret de Inchidere'], df['Media Mobila 100'],
                 where=above_mask, alpha=0.2, color='green', label='Peste media 100 zile')

plt.title('Simulare Piata de Actiuni - 2 ani')
plt.xlabel('Data')
plt.ylabel('Pret ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
