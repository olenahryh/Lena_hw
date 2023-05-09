# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# Python homework 6 

# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

# +
# 2. Загрузите набор данных фильмов в pandas.

movies = pd.read_csv(r'C:\Users\Asus\Desktop\PYTHON\movies.csv')
print(movies)

# +
# 3. Перечислите все столбцы набора данных и изучите их типы. Изучите статистику
# по различным областям. Опишите, какие данные у нас есть.


# Завдяки запитам нижче, ми можеме побачити багато інформації, щодо цього дата-сету! 
# Скільки ми маємо колонок, рядків, які типи данних мають колонки, чи є в таблиці нулі, як виглядають данні про специфічний
# фільм і багато іншого!



# +
# Ми маємо колонки з назвами фільмів; жанри; студія, що розробила фільм; оцінку, яку оцінку дали глядачі кожному фільму;
# рік випуску і багато іншого

movies.head(2)
# -

movies.info()

movies.shape

movies.describe()

movies.columns

# +
#в нашому дата-сеті немає жодних пустих значень

movies.isnull().sum()
# -

movies.isnull()

movies.tail

movies.sample()

movies.sample(5)

movies.index

movies.value_counts()

movies.values

# +
# Бачимо, що немає жодних пустих значень

movies.isna().sum()

# +
# Бачимо, що в таблиці є 2 дублікати

movies.duplicated().sum()

# +
# Тут ми бачимо скільки фільмів було створено кожного року (найбільше у 2008 та 2010 роках)

movies['Year'].value_counts()

# +
# Тут ми бачимо, скільки фільмів було відзнято по кожному жанру (комедій набагато більше)
# Також видно, що деякі однакові жанри записані по-різному (Comedy-Comdy-comedy; Romance-romance-Romence)
# Для того, щоб мати точні данні та користуватися ними для статистики, ми можемо виправити цю помилку!

movies['Genre'].value_counts()
# -

mov = {"Romence" : 'Romance', "romance" : 'Romance', "Comdy": 'Comedy', "comedy" : 'Comedy'}
movies2=movies.replace({"Genre": mov})

# +
# Зараз можемо зручно та спокійно користуватися данними для аналізу. Більше немає дублікатних, 
# неправильно прописаних назв жанрів.

movies2['Genre'].value_counts()

# +
# Отримали такі ж дані, що і з кодом вище, але у вигляді графіку

sns.set_style('whitegrid')
plt.figure(figsize=(8,4))
sns.countplot(x = 'Genre', data = movies2, order = movies2['Genre'].value_counts().index)

# +
# Бачимо, що Fantasy має найбільший відсоток від глядачів

sns.barplot(x='Genre', y='Audience score %', data= movies2)
plt.ylabel('Audience score')
plt.title('Score')

# +
# Хоча,найбільш популярним жінром є Fantasy, більше всього відсотків отримали фільми у жанрі Animation and Drama

best_movie = movies2[(movies2['Audience score %'] == movies2['Audience score %'].max())]
print(best_movie)

# +
# Завдяки цьому графіку ми бачимо, яка компанія відзняла найбільше фільмів (це Independent)

sns.set_style('whitegrid')
plt.figure(figsize=(20,4))
sns.countplot(x = 'Lead Studio', data = movies2, order = movies2['Lead Studio'].value_counts().index);
# -

movies2['Lead Studio'].value_counts(sort=True)

# +
# За допомогою данного коду ми можемо побачити, що студія Independent розробила більше фільмів у жанрі Romance
# Навела також графік, щоб було наглядно видно

ind_movies = movies2[movies2['Lead Studio'] == 'Independent']
print(ind_movies.groupby(['Genre','Lead Studio'])['Genre'].count().sort_values(ascending=False))



sns.set_style('whitegrid')
plt.figure(figsize=(7,4))
sns.countplot(x = 'Genre', data = ind_movies, order = ind_movies['Genre'].value_counts().index);

# +
# 4. Сколько всего фильмов в наборе данных?

movies['Film'].nunique()

# данний код показує, що усього 75 фільмів у наборі даних

# +
# 5. Сколько фильмов содержится в наборе данных за каждый год?

amount_movies = movies['Year'].value_counts()
print(amount_movies)

# +
# 6. Покажите подробную информацию о наименее и наиболее прибыльных
# фильмах в наборе данных

# Найбільш прибутковим є фільм: Life as We Know It
# Найменш прибутковим є: Waiting For Forever

profitability = movies[(movies['Worldwide Gross'] == movies['Worldwide Gross'].min()) 
                       | (movies['Worldwide Gross'] == movies['Worldwide Gross'].max())]
print(profitability)

# +
# 7. Значение «Жанр» временами кажется непоследовательным; попробуйте найти
# эти несоответствия и исправить их.

''' Бачимо, що справді деякі однакові жанри записані по-різному (Comedy-Comdy-comedy; Romance-romance-Romence)
Але таких данних небагато, тому вони не завадять нам зрозуміти більш менш чітку ститистику у майбутньому, 
якщо ми їх видалимо!

Спочатку я пропишу код для видалення цих данних з дата-сету, а потім пропишу ще один варінт, як виправити цю помилку 
(просто зроблю replace на неправильно прописані жанри). Таким чином ми маємо 2 варіанти для вирішення цієї проблеми '''

movies['Genre'].value_counts()

# +
# Знаходимо індекс потрібних нам строк, щоб надалі видалити їх з дата-сету (дублікатні, неправильно прописані типи жанрів)

ind = movies[movies['Genre'] == 'Romence'].index
print(ind)
# -

ind = movies[movies['Genre'] == 'romance'].index
print(ind)

ind = movies[movies['Genre'] == 'Comdy'].index
print(ind)

ind = movies[movies['Genre'] == 'comedy'].index
print(ind)

# +
# Видаляємо за допомогою знайдених індексів 4 неправильно прописаних жанрів

movies_new = movies.drop([43, 72, 47, 76])

# +
# Після видалення, ми бачимо, що дублікатні, невірно прописані види жанрів зникли з дата-сету

movies_new['Genre'].value_counts()
# -

''' Тепер я пропишу варінт REPLACE цих рядків, щоб не роботи видалення даних, оскільки це не є дійсно правильним
рішенням '''

movies['Genre'].value_counts()

mov = {"Romence" : 'Romance', "romance" : 'Romance', "Comdy": 'Comedy', "comedy" : 'Comedy'}
movies2=movies.replace({"Genre": mov})

# +
# Ми бачимо, що вже немає невірно написанх жанрів у дата-сеті! Все прописано коректно, помилка виправлена 

movies2['Genre'].value_counts()

# +
# 8. Сохраните (в новый файл CSV) 10 лучших комедий по количеству зрителей;
# покажите только название фильма, год и студию 


df_top10 = movies.nlargest(10, ['Audience score %'])[['Film', 'Lead Studio', 'Year']]
print(df_top10)
df_top10.to_csv('best_comedies.csv', index=False)
# -

movies1 = pd.read_csv(r'C:\Users\Asus\Desktop\PYTHON\best_comedies.csv')
print(movies1)

# +
# 9. Используйте pip для установки двух библиотек: lxml, MySQL-connector-python

# !pip install lxml
# -

import lxml




import mysql.connector
