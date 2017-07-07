# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

big_fish = media.Movie("Big Fish", "An odd story about a man",
                       "https://upload.wikimedia.org/wikipedia/en/4/41/Big_Fish_movie_poster.png",
                       "https://www.youtube.com/watch?v=dF-Iy7vIOJA")

hackers = media.Movie("Hackers", "A group of hackers fight for freedom",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=Ql1uLyuWra8")

lock_stock = media.Movie("Lock, Stock and Two Smoking Barrels", "Friends put money together to gamble",
                         "https://upload.wikimedia.org/wikipedia/en/e/e9/Lock%2C_Stock_and_Two_Smoking_Barrels_2.jpg",
                         "https://www.youtube.com/watch?v=Y8MXn5No1Jc")

snatch = media.Movie("Snatch", "A large diamond goes missing, and crazy stuff happens",
                     "https://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
                     "https://www.youtube.com/watch?v=Q8jbt0wBkMI")

schindlers_list = media.Movie("Schindler's List", "A movie set in WWII",
                              "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                              "https://www.youtube.com/watch?v=JdRGC-w9syA")

inception = media.Movie("Inception", "A movie about people who steal information in dreams",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

toy_story = media.Movie("Toy Story", "Woody the toy that comes to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc" )

avatar = media.Movie("Avatar", "A movie about people destroying natives","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
movies = [toy_story, avatar, inception, schindlers_list,snatch,lock_stock,big_fish,hackers]
fresh_tomatoes.open_movies_page(movies)
