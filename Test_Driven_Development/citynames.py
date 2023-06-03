from city_functions import get_city_details

print("Enter 'q' at any time to quity.")
while True:
    city_name = input("\nPlease give your city name: ")
    if city_name == 'q':
        break
    country_name = input("Please give your country name: ")
    if country_name == 'q':
        break
    full_details = get_city_details(city_name, country_name)
    print("\t country details are: " + full_details + '.')
