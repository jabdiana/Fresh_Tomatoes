import media
import fresh_tomatoes


Fight_Club = media.Movie("Fight Club",
                    "https://telemachusunedited.files.wordpress.com/2011/07/fight-club-movie-poster-1999.jpg",
                    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

Fast_And_Furious_7 = media.Movie("Fast & Furious 7",
                   "http://www.coverwhiz.com/content/Fast-And-Furious-7.jpg",
                   "https://www.youtube.com/watch?v=yISKeT6sDOg")

Deadpool = media.Movie("Deadpool",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=tLmStxxzhkI")

SWAT = media.Movie("S.W.A.T.",
                   "http://www.imfdb.org/images/a/a5/SWAT2003.jpg",
                   "https://www.youtube.com/watch?v=bq09RP2qizg")

Dark_Knight = media.Movie("The Dark Knight",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

Zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")

Iron_Man_3 = media.Movie("Iron Man 3",
                       "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                       "https://www.youtube.com/watch?v=oYSD2VQagc4")

Big_Hero_6 = media.Movie("Big Hero 6",
                          "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                          "https://www.youtube.com/watch?v=z3biFxZIJOQ")

Dr_Strange = media.Movie("Dr.Strange",
                         "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                         "https://www.youtube.com/watch?v=wwcSki7r9cQ")

Moana = media.Movie("Moana",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

Creed = media.Movie("Creed",
                    "https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg",
                    "https://www.youtube.com/watch?v=Uv554B7YHk4")

Friends_With_Benefits = media. Movie("Friends With Benefits",
                                     "https://upload.wikimedia.org/wikipedia/en/4/4e/Friends_with_benefits_poster.jpg",
                                     "https://www.youtube.com/watch?v=iJS-wWqVAyk")

Shooter = media.Movie("Shooter",
                      "http://www.imfdb.org/images/f/f3/Shooter-Poster.jpg",
                      "https://www.youtube.com/watch?v=6ZVcPhDt-kM")

Lone_Survivor = media.Movie("Lone Survivor",
                        "https://upload.wikimedia.org/wikipedia/en/b/bd/Lone_Survivor_poster.jpg",
                        "https://www.youtube.com/watch?v=yoLFk4JK_RM")

Central_Intelligence = media.Movie("Central Intelligence",
                                   "http://www.imfdb.org/images/c/c4/CI.jpg",
                                   "https://www.youtube.com/watch?v=MxEw3elSJ8M")

Avengers = media.Movie("Avengers",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

Now_You_See_Me = media.Movie("Now You See Me",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")

Civil_War = media.Movie("Civil War",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=dKrVegVI0Us")


movies = [Fight_Club,Fast_And_Furious_7,Deadpool,SWAT,Dark_Knight,Zootopia,Iron_Man_3,Big_Hero_6,Dr_Strange,Moana,Creed, Friends_With_Benefits,
          Shooter,Lone_Survivor,Central_Intelligence,Avengers,Now_You_See_Me,Civil_War]

fresh_tomatoes.open_movies_page (movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
