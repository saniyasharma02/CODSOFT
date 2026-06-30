import pandas as pd
import random

# Load Dataset
try:
    data = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Error: data.csv file not found!")
    exit()


def line():
    print("=" * 55)


def title():
    line()
    print("        SMART RECOMMENDATION SYSTEM")
    line()


def show_categories():
    print("\nChoose a Category:")
    print("1. Movies")
    print("2. Books")
    print("3. Music")
    print("4. Exit")


def get_category(choice):
    category_map = {
        "1": "Movie",
        "2": "Book",
        "3": "Music"
    }
    return category_map.get(choice)


def get_genres(category):
    genres = sorted(
        data[data["Category"] == category]["Genre"].unique()
    )

    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")

    return genres
def get_titles(category, genre):
    filtered = data[
        (data["Category"] == category) &
        (data["Genre"] == genre)
    ]

    titles = filtered["Title"].tolist()

    print(f"\nAvailable {category} Titles:")
    for i, item in enumerate(titles, start=1):
        print(f"{i}. {item}")

    return titles


def get_favourite(titles):
    while True:
        favourite = input("\nEnter your favourite title exactly as shown: ").strip()

        if favourite in titles:
            return favourite

        print("Invalid title! Please enter a title from the list.")


def recommend_items(category, genre, favourite):
    filtered = data[
        (data["Category"] == category) &
        (data["Genre"] == genre)
    ]

    recommendations = filtered["Title"].tolist()

    # Remove favourite item
    if favourite in recommendations:
        recommendations.remove(favourite)

    if len(recommendations) == 0:
        print("\nNo recommendations available.")
        return

    print("\nRecommended For You")
    print("-" * 25)

    random.shuffle(recommendations)

    for item in recommendations[:3]:
        print(f"⭐ {item}")
def continue_program():
    while True:
        choice = input("\nWould you like another recommendation? (Y/N): ").strip().upper()

        if choice == "Y":
            return True
        elif choice == "N":
            print("\nThank you for using the Smart Recommendation System!")
            return False
        else:
            print("Please enter Y or N.")
def main():
    while True:

        title()
        show_categories()

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "4":
            print("\nThank you for using the Smart Recommendation System!")
            break

        category = get_category(choice)

        if category is None:
            print("\nInvalid category! Please try again.")
            continue

        genres = get_genres(category)

        genre = input("\nEnter Genre exactly as shown: ").strip()

        # Case-insensitive matching
        matched_genre = None

        for g in genres:
            if g.strip().lower() == genre.strip().lower():
                matched_genre = g
                break

        if matched_genre is None:
            print("\nInvalid Genre!")
            continue

        genre = matched_genre

        titles = get_titles(category, genre)

        favourite = get_favourite(titles)

        recommend_items(category, genre, favourite)

        if not continue_program():
            break


if __name__ == "__main__":
    main()
