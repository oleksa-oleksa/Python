import webbrowser

class Movie():
    """This class provedes a way to story movie related information"""
    def __init__(self, movie_title, movie_storyline, movie_image_url, movie_trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image_url
        self.trailer_youtube_url = movie_trailer_url
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)