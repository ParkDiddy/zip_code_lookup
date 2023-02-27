# import urlopen and json libraries
from urllib.request import urlopen
import json

# URL of the JSON data to be retrieved
url = "https://raw.githubusercontent.com/millbj92/US-Zip-Codes-JSON/master/USCities.json"

# Attempt to open the URL and retrieve the data
try:
    # Open the URL and read the data
    response = urlopen(url)
    zip_data = json.loads(response.read())
# If an error occurs, display a message and exit the program
except BaseException:
    print("No Response.")
    quit()


def zip_city_lookup():
    # Create an empty list to store matches
    match = []
    # Store keys of the JSON data
    zi = "zip_code"
    ci = "city"
    st = "state"
    co = "county"
    while True:
        request = input("Enter City or Zip Code:\n")
        # Check if input is empty
        if not request:
            print("You didn't enter any input!")
            continue
        # Check if input is a number
        if request.isdigit() and 2 < len(str(request)) < 6:
            request = int(request)
            # Iterate through the JSON data
            for i in zip_data:
                # Check if the request matches the zip code
                if i.get(zi) == request:
                    # Append the match to the match list
                    match.append(
                        {"city": i.get(ci), "state": i.get(st), "county": i.get(co)})
            if match:
                # Iterate through the match list and print the matches
                for matches in match:
                    print(f"{matches.get('city')}, {matches.get('state')}\n"
                          f"{matches.get('county')} County")
                return
        elif request.replace("-", "").isdigit() or request.replace(".", "").isdigit():
            print("Not a valid zip code!")
        elif isinstance(request, str):
            request = request.title()
            # Iterate through the JSON data
            for i in zip_data:
                if i.get(ci) == request:
                    match.append(
                        {"zip": i.get(zi), "state": i.get(st), "county": i.get(co)})
            if match:
                for matches in match:
                    print(f'{matches.get("zip")}, {matches.get("state")}\n'
                          f'{matches.get("county")} County')
                return
            else:
                print("Not a valid city!")


zip_city_lookup()
