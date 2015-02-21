import fresh_tomatoes
"""Function used to create Movie website"""
import media

""" class Movie instances
        _init_gets called
        udacity=Instance Name
        movie_title= Movie Title
        movie_storyline= Movie Storyline
        poster_image= Poster Lin
        trailer_youtube=Trailer Youtube Link"""

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to live",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an Alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=EgHI4YBXhxM")

school_of_rock = media.Movie("School of Rock", "We don't need no education",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "He's dying to become a chef",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Strange things happen after midnight",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "A sci-fi game of survival",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")


movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
"""Movies array listing all the movies"""
fresh_tomatoes.open_movies_page(movies)
"""calls fresh tomatoes file and creates Movie Website"""
