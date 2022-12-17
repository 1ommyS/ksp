def columns(args, number_of_column):
    Arr = args
    number_of_column = str(number_of_column)
    if number_of_column == "Time":
        return Arr[0]
    elif number_of_column == "Velocity":
        return Arr[1]
    elif number_of_column == "Gforce":
        return Arr[2]
    elif number_of_column == "TWR":
        return Arr[3]
    elif number_of_column == "Mass":
        return Arr[4]
    elif number_of_column == "AltitudeFromTerrain":
        return Arr[5]
    elif number_of_column == "DownrangeDistance":
        return Arr[6]
    elif number_of_column == "Latitude":
        return Arr[7]
    elif number_of_column == "Apoapsis":
        return Arr[8]
    elif number_of_column == "Periapsis":
        return Arr[9]
    elif number_of_column == "OrbitalVelocity":
        return Arr[10]
    else:
        return print("некорректное название поля")
