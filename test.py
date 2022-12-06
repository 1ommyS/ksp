def Columns(args, numberOfColumn):
    Arr = args
    numberOfColumn = str(numberOfColumn)
    if numberOfColumn == "Time":
        return Arr[0]
    elif numberOfColumn == "Velocity":
        return Arr[1]
    elif numberOfColumn == "Gforce":
        return Arr[2]
    elif numberOfColumn == "TWR":
        return Arr[3]
    elif numberOfColumn == "Mass":
        return Arr[4]
    elif numberOfColumn == "AltitudeFromTerrain":
        return Arr[5]
    elif numberOfColumn == "DownrangeDistance":
        return Arr[6]
    elif numberOfColumn == "Latitude":
        return Arr[7]
    elif numberOfColumn == "Apoapsis":
        return Arr[8]
    elif numberOfColumn == "Periapsis":
        return Arr[9]
    elif numberOfColumn == "OrbitalVelocity":
        return Arr[10]
    else:
        return print("non-correct data name")
