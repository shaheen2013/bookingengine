## Request example:

http://localhost:8000/api/v1/units/?max_price=100&check_in=2021-12-09&check_out=2021-12-12


## Response example:

    {
        "items": [
            {
                "listing_type": "Apartment",
                "title": "Luxurious Studio",
                "country": "UK",
                "city": "London",
                "price": "40"

            },
            {
                "listing_type": "Hotel",
                "title": "Hotel Lux 3***",
                "country": "BG",
                "city": "Sofia",
                "price": "60" # This the price of the first Hotel Room Type with a Room without blocked days in the range

            },
            {
                "listing_type": "Apartment",
                "title": "Excellent 2 Bed Apartment Near Tower Bridge",
                "country": "UK",
                "city": "London",
                "price": "90"
            },
        ]
    }

# Changes

## New Model
I've created model for block days at ```listing/models.py/BookedListing```
This model contains checkin and checkout who are responsible for putting reservations.


## New endpoint 
I've created new endpoint at ```listing/urls.py``` file named ```api/v1/units/``` and it's returned ```UnitView```
In this end point you can filter listing (Hotel/Apartment) by `max_price`, `checkin` and `checkout` date 

