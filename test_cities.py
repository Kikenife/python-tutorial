from city_functions import city_function

def test_city_country():
    """Do names like this works: 'calgary canada'"""
    formatted_name = city_function('calgary', 'canada')
    assert formatted_name == 'Calgary, Canada'

def test_city_country_population():
    """Do input like this works 'calgary canada population - 10000'"""
    formatted_name = city_function('calgary', 'canada', population=50_000)
    assert  formatted_name == 'Calgary, Canada - population 50000'