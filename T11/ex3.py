import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
user_ids = []
movie_ids = []
ratings = []

for user_id in range(1, 1001):
    num_ratings = np.random.randint(1, 6)
    movies = np.random.choice(range(1, 101), size=num_ratings, replace=False)
    for movie in movies:
        user_ids.append(user_id)
        movie_ids.append(movie)
        ratings.append(np.random.randint(1, 6))

remaining = 10000 - len(user_ids)
if remaining > 0:
    extra_users = np.random.randint(1, 1001, size=remaining)
    extra_movies = np.random.randint(1, 101, size=remaining)
    extra_ratings = np.random.randint(1, 6, size=remaining)
    user_ids.extend(extra_users.tolist())
    movie_ids.extend(extra_movies.tolist())
    ratings.extend(extra_ratings.tolist())

df = pd.DataFrame({
    'ID Utilizator': user_ids[:10000],
    'ID Film': movie_ids[:10000],
    'Rating': ratings[:10000]
})

avg_rating = df.groupby('ID Film')['Rating'].mean()
print("Ratingul mediu pentru fiecare film:")
print(avg_rating)

top_5 = avg_rating.nlargest(5)
print("\nTop 5 filme cu cel mai mare rating mediu:")
print(top_5)

rating_counts = df.groupby('ID Film')['Rating'].count()
low_rated = avg_rating[(rating_counts > 50) & (avg_rating < 3.5)]
print("\nFilme cu >50 evaluari si rating mediu sub 3.5:")
print(low_rated)

plt.figure(figsize=(10, 5))
plt.hist(df['Rating'], bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5], edgecolor='black', rwidth=0.8)
plt.title('Distributia Ratingurilor')
plt.xlabel('Rating')
plt.ylabel('Frecventa')
plt.xticks([1, 2, 3, 4, 5])
plt.grid(axis='y')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
top_5.plot(kind='bar')
plt.title('Top 5 Filme - Rating Mediu')
plt.xlabel('ID Film')
plt.ylabel('Rating Mediu')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

movie_stats = pd.DataFrame({
    'Numar Evaluari': rating_counts,
    'Rating Mediu': avg_rating
})

plt.figure(figsize=(10, 5))
plt.scatter(movie_stats['Numar Evaluari'], movie_stats['Rating Mediu'], alpha=0.6)
plt.title('Numar de Evaluari vs Rating Mediu')
plt.xlabel('Numar de Evaluari')
plt.ylabel('Rating Mediu')
plt.grid(True)
plt.tight_layout()
plt.show()
