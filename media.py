import webbrowser
"""needed to make show_trailer function to work"""

class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG", "PG-13", "R"]
    
    def __init__(udacity, movie_title, movie_storyline, poster_image, trailer_youtube):
        udacity.title = movie_title
        udacity.storyline = movie_storyline
        udacity.poster_image_url = poster_image
        udacity.trailer_youtube_url = trailer_youtube
    """Constructor for Movie Class
        Define Instance Variables for Movie Class
        - Movie Title, Storyline, Poster Image, Trailer called by init """
    
    def show_trailer(udacity):
        webbrowser.open(udacity.trailer_youtube_url)
    """ Define function to open show trailer"""


