country_cap = {}

while True:
    country = input("Enter country name: ")

    if country == "":
        break

    if country.lower() in country_cap:
        print(f"The capital city of {country.capitalize()} is {country_cap[country.lower()]}")

    else:
        cap = input("No data found, Please enter capital city name: ")
        country_cap[country.lower()] = cap.lower()

print(country_cap)