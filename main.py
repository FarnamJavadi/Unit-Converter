print("Unit Converter")

# ==== to choose type of conversion ====
unit_change = {1: "Length", 2: "Mass",  3: "Temperature"}

# ==== for getting number of type ====
for keys, values in unit_change.items():
    print("{:2}. {}".format(keys, values))

change = int(input("\nWhich type of conversion you want to do from 1 to 3: "))

# ==== Type 1 (length) ====
if change == 1:
    print("You chose type Length")
    print("")
    length_dict = \
        {
            1: "CM to M",
            2: "M to CM",
            3: "CM to INCH",
            4: "INCH to CM",
            5: "CM to KM",
            6: "KM to CM",
            7: "CM to FOOT",
            8: "FOOT to CM"
        }

    # ==== for getting number of conversion ====
    length_value = float(input("Enter a number to convert: "))
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
    else:
        print("Sorry, Please type correct number from 1 to 8.")

# ==== Type 2 (Mass) ====
elif change == 2:
    print("You chose type Mass")
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
            10: "pound (lb) to Kilogram"
        }

    # ==== for getting number of conversion ====
    mass_value = float(input("Enter a number to convert: "))
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
    else:
        print("Sorry, Please type correct number from 1 to 10.")

# ==== Type 3 (Temperature) ====
elif change == 2:
    print("You chose type Temperature")
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
    Temp_value = float(input("Enter a number to convert: "))
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
else:
    print("Sorry, Please type correct number from 1 to 4.")
