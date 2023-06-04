def get_city_details(city_name, country_name, population=''):
    """Generate a neatly concatenated city details"""
    if population:
        city_details = city_name + " " + country_name + " - population " +  population
    else:
        city_details = city_name + " " + country_name
    return city_details.title()
