import phonenumbers
from test import number
from phonenumbers import geocoder

location_name = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(location_name,"en"))

