from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Gbenga Bamimore' works"""
    formatted_name = get_formatted_name('gbenga', 'bamimore')
    assert formatted_name == 'Gbenga Bamimore'

def test_first_last_middle_name():
    """Do names like 'Gbenga Bamimore' works"""
    formatted_name = get_formatted_name('gbenga', 'bamimore', 'Oribogunje')
    assert formatted_name == 'Gbenga Oribogunje Bamimore'