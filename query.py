# Import the Movies class from movies.py
from movies import Movies

# Initialize the Movies object
movies = Movies('./PythonExercise/movies.txt')

# Lists all movie names
def list_movie_names():
    movie_names = [movie['name'] for movie in movies._movies]
    return ', '.join(movie_names)

# Search movies by name
def search_movies_by_name(keyword):
    result = [movie['name'] for movie in movies._movies if keyword.lower() in movie['name'].lower()]
    return ', '.join(result)

# Search movies by cast
def search_movies_by_cast(keyword):
    results = []
    for movie in movies._movies:
        movie_name = movie['name']
        cast = [actor for actor in movie['cast'] if keyword.lower() in actor.lower()]
        if cast:
            results.append(f'{movie_name}\n{cast}')
    return results

# Main menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. List all movie names")
        print("2. Search movies by name")
        print("3. Search movies by cast")
        print("q. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("All Movie Names:")
            print(list_movie_names())
        elif choice == '2':
            keyword = input("Enter a keyword to search movies by name: ")
            print(f"Movies with '{keyword}' in their names:")
            print(search_movies_by_name(keyword))
        elif choice == '3':
            keyword = input("Enter a keyword to search movies by cast: ")
            print(f"Movies with '{keyword}' in their cast:")
            results = search_movies_by_cast(keyword)
            for result in results:
                print(result)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
