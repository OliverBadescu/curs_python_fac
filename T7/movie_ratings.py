def load_movies(filename):
    movies = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    title, rating = line.rsplit(", ", 1)
                    movies[title] = int(rating)
    except FileNotFoundError:
        pass
    return movies


def save_movies(filename, movies):
    with open(filename, "w") as file:
        for title, rating in movies.items():
            file.write(f"{title}, {rating}\n")


def display_movies(movies):
    if not movies:
        print("List ins empty")
        return
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
    print("\nMovies (sorted by rating):")
    for title, rating in sorted_movies:
        print(f"  {title}: {rating}/5")


def get_valid_rating():
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number")


def main():
    filename = "movies.txt"
    movies = load_movies(filename)

    while True:
        print("\n Movie Rating Program")
        print("1. View all movies")
        print("2. Add a new movie")
        print("3. Update a movie rating")
        print("4. Delete a movie")
        print("5. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_movies(movies)

        elif choice == "2":
            title = input("Enter movie title: ")
            if title in movies:
                print("Movie already exists.")
            else:
                rating = get_valid_rating()
                movies[title] = rating
                save_movies(filename, movies)
                print(f"Added '{title}' with rating {rating}.")

        elif choice == "3":
            title = input("Enter movie title to update: ")
            if title not in movies:
                print("Movie not found.")
            else:
                rating = get_valid_rating()
                movies[title] = rating
                save_movies(filename, movies)
                print(f"Updated '{title}' to rating {rating}.")

        elif choice == "4":
            title = input("Enter movie title to delete: ")
            if title not in movies:
                print("Movie not found.")
            else:
                del movies[title]
                save_movies(filename, movies)
                print(f"Deleted '{title}'.")

        elif choice == "5":
            save_movies(filename, movies)
            print("Changes saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
