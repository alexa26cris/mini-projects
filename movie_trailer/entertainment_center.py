import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Marine on a alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

ready_player_one = media.Movie("Ready Player One",
                               "A Virtual Reality gaming world movie",
                               "https://en.wikipedia.org/wiki/Ready_Player_One_(film)#/media/File:Ready_Player_One_(film).png",
                               "https://www.youtube.com/watch?v=cSp1dM2Vj48")
#ready_player_one.show_trailer()

movies = [toy_story, avatar, ready_player_one]
fresh_tomatoes.open_movies_page(movies)
