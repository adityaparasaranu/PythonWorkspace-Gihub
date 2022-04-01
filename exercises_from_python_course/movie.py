user_input = input("Enter 'a' to add a movie. Enter 'l' to list all the movies. Enter 'f' to find the movies. Enter 'q' to quit : ")

movies = []


while user_input != 'q':
    if user_input == 'a':
        movie_title = input("Enter the movie title : ")
        release_date = input("Enter the release date of movie : ")
        movies.append({'Movie Name' : movie_title, 'Release Date : ' : release_date})

    elif user_input == 'l':
        for movie in movies :
            print(movie)

    elif user_input == 'f':
        finding_name = input("Enter a movie name to check whether the movie is there or not : ")
        for movie in movies :
            if movie.get('Movie Name') == finding_name:
                print("The Movie you entered is found in the movies list")
            else:
                print("The Movie you entered is not found in the movies list")

    else:
        print("Wrong Command. Try again")

    user_input = input("Enter 'a' to add a movie. Enter 'l' to list all the movies. Enter 'f' to find the movies. Enter 'q' to quit : ")