# Examples

I originally typed out a message, mentioning how in the tutorials which I had watched,
the people in the tutorials had create example lists. Both were showing the CRUD practise being
utilised, and one was a list of drinks whilst the other one listed storage locations and
the items within those locations.

### Drinks Example

So the drinks example had a drink model, and you could either create a new drink
within the model by going to `http://127.0.0.1:8000/admin` and creating it via the
site administration. Which, in practise isn't ideal for what we intend.

However, from what was shown, they provided a name for the drink, as well as a
description too.

>**Name:** Orange Soda  
**Description:** carbonated orange flavoured drink

To see the JSON response of this drink, there was a view created for it, so you
could navigate to `http://127.0.0.1:8000/drinks/2` to see the response, using
the Django REST Framework resources.

On the page you would see:

> GET /drinks/2

> HTTP 200 OK  
Allow: PUT, DELETE, GET, OPTIONS  
Content-Type: application/json  
Vary: Accept
> 
> {  
    "id": 2,  
    "name": "Orange Soda",  
    "description": "Carbonated orange flavoured drink."  
}

Along with the ability to change the media type and the content block, to then
"PUT" a new request into the page.

### Storage Loction Example

This was similar, but the tutorial showed the locations being created, and they
all had their own unique primary key id which could be later referenced.

The locations were along the lines of:

- Shed
- Trunk
- Garage
- Storage Locker
- Attic

After that, they created some items go into those locations.

It doesn't matter what items they created, but the thing is, is that they assigned
these items to the locations.

A lawnmower might've been assigned to id `1` for example though, meaning it was
placed within the shed. 

Once a variety of items were created and assigned to these locations, the person
in the tutorial showed how they could go to `127.0.0.1/5000/locations/1` and you would
see all the items assigned to that location.

```.json
{
    "items": [
        {
            "id": 1,
            "item_name": "lawnmower",
            "item_loc": 1
        },
        {
            "id": 2,
            "item_name": "shovel",
            "item_loc": 1            
        },
        {
            "id": 3,
            "item_name": "rake",
            "item_loc": 1
        },
    ]
}
```


