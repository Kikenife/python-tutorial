def city_function(city_name, country_name, population=0):

    output_string = f"{city_name.title()}, {country_name.title()}"
    if population:
        output_string += f" - population {population}"
    else:
        output_string
    return output_string