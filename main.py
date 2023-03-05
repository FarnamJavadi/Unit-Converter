print("Unit Converter")
print("===============")

# ==== to choose type of conversion ====
unit_change = \
    {
        1: "Length",
        2: "Mass",
        3: "Temperature",
        4: "Time",
        5: "Spead",
        6: "Energy",
        7: "Pressure"
    }

# ==== for getting number of type ====
for keys, values in unit_change.items():
    print("{:2}. {}".format(keys, values))

change = int(input("\nWhich type of conversion you want to do from 1 to 7: "))

# ==== Type 1 (length) ====
if change == 1:
    print(">>> You chose type Length")
    print("")
    length_dict = \
        {
            1: "Centimeter to Meter",
            2: "Meter to Centimeter",
            3: "Centimeter to INCH",
            4: "INCH to Centimeter",
            5: "Centimeter to KiloMetre",
            6: "KiloMetre to Centimeter",
            7: "Centimeter to FOOT",
            8: "FOOT to Centimeter",
            9: "Kilometre to Mile",
            10: "Mile to Kilometre"
        }

    # ==== for getting number of conversion ====
    print("==========================")
    length_value = float(input("- Enter a number to convert: "))
    for keys, values in length_dict.items():
        print("{:2}. {}".format(keys, values))
    length_convert = int(input("\nWhich conversion you want to do from 1 to 8: "))

    # ==== converting ====
    if length_convert == 1:
        print("{} cm is equal to {} m.".format(length_value, length_value / 100))
    elif length_convert == 2:
        print("{} m is equal to {} cm.".format(length_value, length_value * 100))
    elif length_convert == 3:
        print("{} cm is equal to {} inch.".format(length_value, length_value / 2.54))
    elif length_convert == 4:
        print("{} inch is equal to {} cm.".format(length_value, length_value * 2.54))
    elif length_convert == 5:
        print("{} cm is equal to {} km.".format(length_value, length_value / 100000))
    elif length_convert == 6:
        print("{} km is equal to {} cm.".format(length_value, length_value * 100000))
    elif length_convert == 7:
        print("{} cm is equal to {} feet.".format(length_value, length_value / 30.48))
    elif length_convert == 8:
        print("{} feet is equal to {} cm.".format(length_value, length_value * 30.48))
    elif length_convert == 9:
        print("{} KM is equal to {} mile".format(length_value, length_value / 1.609))
    elif length_convert == 10:
        print("{} mile is equal to {} KM".format(length_value, length_value * 1.609))
    else:
        print("Sorry, Please type correct number from 1 to 10.")

# ==== Type 2 (Mass) ====
elif change == 2:
    print(">>> You chose type Mass")
    print("")
    mass_dict = \
        {
            1: "Gram to Kilogram",
            2: "Kilogram to Gram",
            3: "Kilogram to Tonne",
            4: "Tonne to Kilogram",
            5: "Milligram to Kilogram",
            6: "Kilogram to Milligram",
            7: "Milligram to Gram",
            8: "Gram to Milligram",
            9: "kilogram to pound (lb)",
            10: "pound (lb) to Kilogram",
            11: "Micrograms to gram",
            12: "Micrograms to Kilogram"
        }

    # ==== for getting number of conversion ====
    print("==========================")
    mass_value = float(input("- Enter a number to convert: "))
    for keys, values in mass_dict.items():
        print("{:2}. {}".format(keys, values))
    mass_convert = int(input("\nWhich conversion you want to do from 1 to 10: "))

    # ==== converting ====
    if mass_convert == 1:
        print("{} g is equal to {} Kg".format(mass_value, mass_value / 1000))
    elif mass_convert == 2:
        print("{} Kg is equal to {} g".format(mass_value, mass_value * 1000))
    elif mass_convert == 3:
        print("{} kg is equal to {} T".format(mass_value, mass_value / 1000))
    elif mass_convert == 4:
        print("{} T is equal to {} kg".format(mass_value, mass_value * 1000))
    elif mass_convert == 5:
        print("{} mg is equal to {} kg".format(mass_value, mass_value / 1000000))
    elif mass_convert == 6:
        print("{} Kg is equal to {} mg".format(mass_value, mass_value * 1000000))
    elif mass_convert == 7:
        print("{} mg is equal to {} g".format(mass_value, mass_value / 1000))
    elif mass_convert == 8:
        print("{} g is equal to {} mg".format(mass_value, mass_value * 1000))
    elif mass_convert == 9:
        print("{} Kg is equal to {} lb".format(mass_value, mass_value * 2.20462))
    elif mass_convert == 10:
        print("{} lb is equal to {} kg".format(mass_value, mass_value / 2.20462))
    elif mass_convert == 11:
        print("{} μg is equal to {} g".format(mass_value, mass_value / 1e+6))
    elif mass_convert == 12:
        print("{} μg is equal to {} Kg".format(mass_value, mass_value / 1e+9))
    else:
        print("Sorry, Please type correct number from 1 to 12.")

# ==== Type 3 (Temperature) ====
elif change == 3:
    print(">>> You chose type Temperature")
    print("")
    Temp_dict = \
        {
            1: "Celsius to Fahrenheit",
            2: "Celsius to Kelvin",
            3: "Fahrenheit to Celsius",
            4: "Fahrenheit to Kelvin",
            5: "Kelvin to Celsius",
            6: "Kelvin to Fahrenheit"
        }

    # ==== for getting number of conversion ====
    print("==========================")
    Temp_value = float(input("- Enter a number to convert: "))
    for keys, values in Temp_dict.items():
        print("{:2}. {}".format(keys, values))
    Temp_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))

    # ==== converting ====
    if Temp_convert == 1:
        print("{} C is equal to {} F".format(Temp_value, (Temp_value * 9.5) + 32))
    elif Temp_convert == 2:
        print("{} C is equal to {} K".format(Temp_value, Temp_value + 273.15))
    elif Temp_convert == 3:
        print("{} F is equal to {} C".format(Temp_value, (Temp_value - 32) * 5.9))
    elif Temp_convert == 4:
        print("{} C is equal to {} K".format(Temp_value, (Temp_value - 32) * 5.9 + 273.15))
    elif Temp_convert == 5:
        print("{} K is equal to {} C".format(Temp_value, Temp_value - 273.15))
    elif Temp_convert == 6:
        print("{} K is equal to {} F".format(Temp_value, (Temp_value - 273.15) * 9.5 + 32))
    else:
        print("Sorry, Please type correct number from 1 to 6.")

# ==== Type 4 (Time) ====
elif change == 4:
    print(">>> You chose type Time")
    print("")
    Time_dict = \
        {
            1: "Second to Minute",
            2: "Minute to Second",
            3: "Second to Hour",
            4: "Minute to Hour",
            5: "Hour to Minute",
            6: "Day to Hour",
            7: "Hour to Day"
        }

    # ==== for getting number of conversion ====
    print("==========================")
    Time_value = float(input("- Enter a number to convert: "))
    for keys, values in Time_dict.items():
        print("{:2}. {}".format(keys, values))
    Time_convert = int(input("\nWhich conversion you want to do from 1 to 7: "))

    # ==== converting ====
    if Time_convert == 1:
        print("{} S is equal to {} M".format(Time_value, Time_value / 60))
    elif Time_convert == 2:
        print("{} M is equal to {} S".format(Time_value, Time_value * 60))
    elif Time_convert == 3:
        print("{} S is equal to {} H".format(Time_value, Time_value / 3600))
    elif Time_convert == 4:
        print("{} M is equal to {} H".format(Time_value, Time_value / 60))
    elif Time_convert == 5:
        print("{} H is equal to {} M".format(Time_value, Time_value * 60))
    elif Time_convert == 6:
        print("{} day is equal to {} H".format(Time_value, Time_value * 24))
    elif Time_convert == 7:
        print("{} H is equal to {} day".format(Time_value, Time_value / 24))
    else:
        print("Sorry, Please type correct number from 1 to 7.")

# ==== Type 5 (Speed) ====
elif change == 5:
    print(">>> You chose type Spead")
    print("")
    Spead_dict = \
        {
            1: "Mile per hour to kilometer per hour",
            2: "Kilometer per hour to Mile per hour",
            3: "Mile per hour to Meter per Second",
            4: "Meter per Second to Mile per hour",
            5: "Kilometer per hour to Meter per Second",
            6: "Meter per Second to Kilometer per hour"
        }

    # ==== for getting number of conversion ====
    print("==========================")
    Spead_value = float(input("- Enter a number to convert: "))
    for keys, values in Spead_dict.items():
        print("{:2}. {}".format(keys, values))
    Spead_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))

    # ==== converting ====
    if Spead_convert == 1:
        print("{} Ml is equal to {} Km".format(Spead_value, Spead_value * 1.609))
    elif Spead_convert == 2:
        print("{} Km is equal to {} Ml".format(Spead_value, Spead_value / 1.609))
    elif Spead_convert == 3:
        print("{} Ml is equal to {} M".format(Spead_value, Spead_value / 2.237))
    elif Spead_convert == 4:
        print("{} M is equal to {} Ml".format(Spead_value, Spead_value * 2.237))
    elif Spead_convert == 5:
        print("{} Km is equal to {} M".format(Spead_value, Spead_value / 3.6))
    elif Spead_convert == 6:
        print("{} M is equal to {} Km ".format(Spead_value, Spead_value * 3.6))
    else:
        print("Sorry, Please type correct number from 1 to 6.")

# ==== Type 6 (Energy) ====
elif change == 6:
    print(">>> You chose type Energy")
    print("")
    Energy_dict = \
        {1: "Joule to Kilojoule",
         2: "Kilojoule to Joule",
         3: "Joule to Kilocalorie",
         4: "Kilocalorie to Joule",
         5: "Kilojoule to Kilocalorie",
         6: "Kilocalorie to Kilojoule"
         }

    # ==== for getting number of conversion ====
    print("==========================")
    Energy_value = float(input("- Enter a number to convert: "))
    for keys, values in Energy_dict.items():
        print("{:2}. {}".format(keys, values))
    Energy_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))
    if Energy_convert == 1:
        print("{} J is equal to {} Kj".format(Energy_value, Energy_value / 1000))
    elif Energy_convert == 2:
        print("{} Kj is equal to {} J".format(Energy_value, Energy_value * 1000))
    elif Energy_convert == 3:
        print("{} J is equal to {} Kc".format(Energy_value, Energy_value / 4184))
    elif Energy_convert == 4:
        print("{} Kc is equal to {} J".format(Energy_value, Energy_value * 4184))
    elif Energy_convert == 5:
        print("{} Kj is equal to {} Kc".format(Energy_value, Energy_value / 4.184))
    elif Energy_convert == 6:
        print("{} Kc is equal to {} Kj".format(Energy_value, Energy_value * 4.184))
    else:
        print("Sorry, Please type correct number from 1 to 6.")

# ==== Type 7 (Pressure) ====
elif change == 7:
    print(">>> You chose type Pressure")
    print("")
    Pressure_dict = \
        {
            1: "Bar to Pascal",
            2: "Bar to Standard atmosphere",
            3: "Pascal to Bar",
            4: "Pascal to Standard atmosphere",
            5: "Standard atmosphere to Pascal",
            6: "Standard atmosphere to Bar"
        }
    # ==== for getting number of conversion ====
    print("==========================")
    Pressure_value = float(input("- Enter a number to convert: "))
    for keys, values in Pressure_dict.items():
        print("{:2}. {}".format(keys, values))
    Pressure_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))

    # ==== converting ====
    if Pressure_convert == 1:
        print("{} Bar is equal to {} P".format(Pressure_value, Pressure_value * 100000))
    elif Pressure_convert == 2:
        print("{} Bar is equal to {} atm".format(Pressure_value, Pressure_value / 1.013))
    elif Pressure_convert == 3:
        print("{} P is equal to {} Bar".format(Pressure_value, Pressure_value / 100000))
    elif Pressure_convert == 4:
        print("{} P is equal to {} atm".format(Pressure_value, Pressure_value / 101300))
    elif Pressure_convert == 5:
        print("{} atm is equal to {} P".format(Pressure_value, Pressure_value * 101300))
    elif Pressure_convert == 6:
        print("{} atm is equal to {} Bar".format(Pressure_value, Pressure_value * 1.013))
    else:
        print("Sorry, Please type correct number from 1 to 6.")
else:
    print("Sorry, Please type correct number from 1 to 7.")

print("farnamjavadi.com")
