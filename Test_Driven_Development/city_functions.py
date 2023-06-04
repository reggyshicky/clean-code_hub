def get_city_details(city_name, country_name, population):
    """Generate a neatly concatenated city details"""
    city_details = city_name + " " + country_name + " - population " +  population
    return city_details.title()
