print("Welcome to Unit Converter")
unit_dict = {1: "CM to M", 2: "M to CM", 3: "CM to INCH", 4: "INCH to CM", 5: "CM to KM", 6: "KM to CM", 7: "CM to FEET", 8: "FEET to CM", 9: "CENTIGRADE to FAHRENHIET", 10: "FAHRENHIET to CENTIGRADE"}

value = float(input("Enter a number: "))
for keys, values in unit_dict.items():
    print("{:2}. {}".format(keys, values))

convert = int(input("\nWhich conversion you want to do from 1 to 10: "))

if convert == 1:
    print("{} cm is equal to {} m.".format(value, value/100))

elif convert == 2:
    print("{} m is equal to {} cm.".format(value, value*100))

elif convert == 3:
    print("{} cm is equal to {} inch.".format(value, value/2.54))

elif convert == 4:
    print("{} inch is equal to {} cm.".format(value, value*2.54))

elif convert == 5:
    print("{} cm is equal to {} km.".format(value, value/100000))

elif convert == 6:
    print("{} km is equal to {} cm.".format(value, value*100000))

elif convert == 7:
    print("{} cm is equal to {} feet.".format(value, value/30.48))

elif convert == 8:
    print("{} feet is equal to {} cm.".format(value, value*30.48))

elif convert == 9:
    print("{} c is equal to {} f.".format(value, (value * 1.8) + 32))

elif convert == 10:
    print("{} f is equal to {} c.".format(value, (value - 32) * 0.555))

else:
    print("Sorry, Please type correct number from 1 to 10.")

print("Thank You for using our unit converter!")
