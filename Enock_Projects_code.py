#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:42:35 2024

@author: avntrainee
"""
import pandas as pd
df_movies=pd.read_csv("/home/avntrainee/DARA2024_Enock/movie_dataset.csv")
print(df_movies)

"""
     Rank                    Title  ... Revenue (Millions) Metascore
0       1  Guardians of the Galaxy  ...             333.13      76.0
1       2               Prometheus  ...             126.46      65.0
2       3                    Split  ...             138.12      62.0
3       4                     Sing  ...             270.32      59.0
4       5            Suicide Squad  ...             325.02      40.0
..    ...                      ...  ...                ...       ...
995   996     Secret in Their Eyes  ...                NaN      45.0
996   997          Hostel: Part II  ...              17.54      46.0
997   998   Step Up 2: The Streets  ...              58.01      50.0
998   999             Search Party  ...                NaN      22.0
999  1000               Nine Lives  ...              19.64      11.0

[1000 rows x 12 columns]
"""

df_cleaned=df_movies.dropna()
print(df_cleaned)

"""
     Rank                     Title  ... Revenue (Millions) Metascore
0       1   Guardians of the Galaxy  ...             333.13      76.0
1       2                Prometheus  ...             126.46      65.0
2       3                     Split  ...             138.12      62.0
3       4                      Sing  ...             270.32      59.0
4       5             Suicide Squad  ...             325.02      40.0
..    ...                       ...  ...                ...       ...
993   994  Resident Evil: Afterlife  ...              60.13      37.0
994   995                 Project X  ...              54.72      48.0
996   997           Hostel: Part II  ...              17.54      46.0
997   998    Step Up 2: The Streets  ...              58.01      50.0
999  1000                Nine Lives  ...              19.64      11.0

[838 rows x 12 columns]
"""

#highest rated movie
df_rate=df_movies["Rating"]
print(df_rate)
print(df_movies["Rating"].max())

df_movies["Revenue (Millions)"]
highest_rated=df_movies.loc[df_movies["Rating"].idxmax(),["Title","Rating"]]
print(highest_rated)


#Rating - 9.0
#Title     The Dark Knight #- Ans


#avg_revenue of all movies

avg_revenue=df_movies["Revenue (Millions)"].mean()
print(avg_revenue)

#82.95637614678898 - Ans


#avg revenue btw 2015 and 2017

avg_revenue_2015_2017=df_movies[(df_movies["Year"]>=2015) & (df_movies["Year"]<=2017)]
avg_revenue_2015_2017_mean=avg_revenue_2015_2017["Revenue (Millions)"].mean()
print(avg_revenue_2015_2017_mean)


#63.099905660377345 - Ans

#movies sold in 2016

df_movies_2016=df_movies[df_movies["Year"]==2016].shape[0]
print(df_movies_2016)

#297 - Ans

#movies directed by christopher Nolan
df_movies_Nolan=df_movies[df_movies["Director"]=="Christopher Nolan"].shape[0]
print(df_movies_Nolan)

#5 - Ans

#Movies with rating of =>8.0

count_movies_ge_8 = df_movies[df_movies["Rating"] >= 8].shape[0]
print(count_movies_ge_8)

#78 - Ans

# Filter movies directed by Christopher Nolan
nolan_movies = df_movies[df_movies["Director"] == "Christopher Nolan"]

# Calculate the median rating
median_rating_nolan = nolan_movies["Rating"].median()
print(median_rating_nolan)

#8.6 - Ans

# Group by year and calculate the average rating
average_rating_per_year = df_movies.groupby("Year")["Rating"].mean()

# Find the year with the highest average rating
yr_highest_avg_rating = average_rating_per_year.idxmax()
highest_avg_rating = average_rating_per_year.max()

print(yr_highest_avg_rating, highest_avg_rating)


#2007 7.133962264150944 -Ans


# Count the number of movies made in 2006
movies_2006 = df_movies[df_movies["Year"] == 2006].shape[0]

# Count the number of movies made in 2016
movies_2016 = df_movies[df_movies["Year"] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(percentage_increase)


#575.0 - Ans


# Split the "Actors" column by comma and explode the list into separate rows
actors_series = df_movies["Actors"].str.split(", ")
all_actors = actors_series.explode()

# Count the occurrences of each actor
actor_counts = all_actors.value_counts()

# Get the most common actor
most_common_actor = actor_counts.idxmax()
most_common_count = actor_counts.max()

print(f"The most common actor is {most_common_actor} with {most_common_count} appearances.")


# Split the "Genre" column by comma and explode the list into separate rows
genres_series = df_movies["Genre"].str.split(", ")
all_genres = genres_series.explode()

# Get the unique genres
unique_genres = all_genres.unique()

# Count the number of unique genres
num_unique_genres = len(unique_genres)

print(num_unique_genres)


















