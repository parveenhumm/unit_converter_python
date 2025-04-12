
def convert_unit(category, value , unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value*0.621371
        elif unit == "miles to kilometers":
            return value/0.621371
        
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value*2.20462
        elif unit == "pounds to kilograms":
            return value/2.20462
        
    elif category == "Time":
        if unit == "hours to minutes":
            return value*60
        elif unit == "minutes to hours":
            return value/60
        elif unit == "hours to days":
            return value*24
        elif unit == "days to hours":
            return value/24
