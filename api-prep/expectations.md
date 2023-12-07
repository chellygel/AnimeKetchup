# API Expectations

For our API, we expect users to be able to perform a nest of
operations to interact with our application and our API, to
consume it and to retrieve the data that they desire.

So to keep this all relative and together, this new directory
has been created called 'api-prep' for any information to be
referred back to at a later date. This directory will not be 
in the final product, only in development temporarily.

Starting off with an example verb/action combination, of a task
a user might be expected to perform.

> **verb**  
> action 

Here is our simple JSON structure:

```.json
{
    "users": [
        {
            "user_id": 1,
            "user_name": "Lee",
            "anime": "Yu Yu Hakusho",
            "anime_eps": 99,
            "eps_desired": 99,
            "eps_watched": 42
        },
        {
            "user_id": 2,
            "user_name": "Chelly",
            "anime": "Sailor Moon",
            "anime_eps": 200,
            "eps_desired": 50,
            "eps_watched": 150
        }
    ]
}
```

This formatting applies throughout these expectations.

> **PUT**  
> Update the current amount of episodes watched.

We might have an API decorated method in our project called "update_user" and we can send a JSON payload in a raw format
to an address.

Example: `http://127.0.0.1:5000/api/update_user`

The payload could look like:

```.json
{
  "users": [
    {
      "user_id": 1,
      "eps_watched": 50
    }
  ]
}
```

The JSON response output we may expect for this could be:

```.json
{
    "users": [
        {
            "user_id": 1,
            "user_name": "Lee",
            "anime": "Yu Yu Hakusho",
            "anime_eps": 99,
            "eps_desired": 99,
            "eps_watched": 50
        },
        {
            "user_id": 2,
            "user_name": "Chelly",
            "anime": "Sailor Moon",
            "anime_eps": 200,
            "eps_desired": 50,
            "eps_watched": 150
        }
    ]
}
```

### Additional Expectations
Rather than providing the expecting JSON response for each expectation, I'll be creating these blocks 
to help visualise what we desire going forward.

> **POST**  
> Add a new user to the database.

> **GET**  
> A user can see the items in their watchlist, their current progress, and also how many
> episodes there are total to watch.

> **DELETE**  
> Delete an anime from the watchlist if a user has completed it.

> **POST**  
> Add a new anime to the watchlist for the user.

> **PUT**  
> When the user is expected to complete watching the anime of their choice, with
> the permutations which they set for their schedule.

> **GET**  
> Allow the user to see how long they have remaining left, and to see if they are on
> track with their schedule.

> **PUT**  
> User wishes to exclude the filler episodes from their watch marathon.

> **GET**  
> A tabulate table with increased formatting to display to the user.

> **DELETE**  
> Delete an anime from the watchlist if a user accidentally added it.

> **POST**  
> Add a new anime to the watchlist for the user.

> **DELETE**  
> Delete a user if they no longer wish to track their progress.

> **GET**  
> Get all the information for the anime. 

> **GET**  
> Search for an anime.

> **GET**  
> Recommend an anime.

There are other expectations we might expect for ourselves too.

> **GET**  
> All the users watching the One Piece anime.