import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of the toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=wmiIUN-7qhE")

avatar = media.Movie("Avatar", 
                        "A marine on the other planet", 
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", 
                        "https://www.youtube.com/watch?v=6ziBFh3V1aM")

school_of_rock =  media.Movie("School of Rock", 
                        "Old rocker on the road", 
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")


ratatouille = media.Movie("Ratatouille", 
                          "Storyline", 
                          "http://upload.wikimedia.org/wikipedia/en/S/SO/RatatouillePoster.jpg", 
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", 
                                "Storyline", 
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", 
                                "https://www.youtube.com/watch?v=atLngQvaU")

hunger_games = media.Movie("Hunger Games", 
                           "Storyline", 
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock ,ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)