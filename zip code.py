from urllib.request import urlopen
import json

# URL of the JSON data to be retrieved
url = "https://raw.githubusercontent.com/millbj92/US-Zip-Codes-JSON/master/USCities.json"

# Attempt to open the URL and retrieve the data
try:
    response = urlopen(url)
    data = json.loads(response.read())
# If an error occurs, display a message and exit the program
except:
    print("No Response.")
    quit()

# Initialize an empty list to store matches
match = []

# Create variables to store the keys of the data
zi = "zip_code"
ci = "city"
st = "state"
co = "county"

while True:
    request = input("Enter City or Zip Code:\n")
    if not request:
        print("You didn't enter any input!")
    elif request.isnumeric():
        if 2 < len(str(request)) < 6:
            request = int(request)
            break
        else:
            print("Invalid Zip Code!")
    else:
        request = request.title()
        break

# Iterate through the data and search for matches
for i in data:
    # Check if the request matches the zip code
    if i.get(zi) == request:
        print(f"\n{i.get(ci)} {i.get(st)}")
        print(f"{i.get(co)} County")
        match.append(i.get(zi))
    # Check if the request matches the city
    elif i.get(ci) == request:
        print(f"\n{str(i.get(zi))} {i.get(st)}")
        print(f"{i.get(co)} County")
        match.append(i.get(zi))

if not match:
    print("Not a valid city!")