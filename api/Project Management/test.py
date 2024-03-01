def find_anime_for_user(username, users):
    # Using a for loop to loop through the dictionary of users.
    for user in users:
        # Check to see if the username matches, and it is being converted to
        # lowercase to match the same version.
        if user['user_name'].lower() == username.lower():
            # Retrieve the watchlist.
            watchlist = user.get('watchlist', [])
            watching_anime = []
            # Iterate through each entry in the user's watchlist to see what
            # anime the user has begun watching.
            for entry in watchlist:
                if entry.get('anime_name') and entry.get('eps_watched') > 0:
                    watching_anime.append(entry['anime_name'])

            # If there is more than anime being watched at a time, the animes
            # will be joined together using the 'join' method and combined with
            # a comma for formatting reasons.
            if watching_anime:
                print(f"{username.lower().capitalize()} "
                      f"is currently watching: {', '.join(watching_anime)}")
                return

            # If the user's episodes watched or "eps_watched" is less than 0,
            # that is considered that the user hasn't begun watching that anime.
            else:
                print(f"{username.lower().capitalize()} "
                      f"has not started watching any anime.")
                # Exits the function ensuring that it doesn't continue searching
                # through the remaining users after finding a match.
                return

    # If none of the users in the list match the user's input, this print
    # statement is provided and printed outside the loop.
    print("That user doesn't exist, or the username was entered incorrectly.")


# Here is our test dictionary, containing our JSON structure.


test_dict = {
    "users": [
        {
            "user_id": 1,
            "user_name": "Lee",
            "watchlist": [
                {
                    "anime_id": 1,
                    "anime_name": "One Piece",
                    "total_eps": 1048,
                    "eps_watched": 1
                },
                {
                    "anime_id": 2,
                    "anime_name": "Utena",
                    "total_eps": 39,
                    "eps_watched": 1
                }
            ]
        },
        {
            "user_id": 2,
            "user_name": "Chelly",
            "watchlist": [
                {
                    "anime_id": 1,
                    "anime_name": "One Piece",
                    "total_eps": 1048,
                    "eps_watched": 542
                }
            ]
        }
    ]
}

# Takes in a user input for the username.
user_name_input = input("Enter your username: ")

# Calls the function that we have defined, with the user input and the list of
# users from the test dictionary.
find_anime_for_user(user_name_input, test_dict['users'])
