input_month = input("Enter the month: ").capitalize()  # Ensures first letter is capitalized
input_day = int(input("Enter the day: "))

if (input_month == "January" and input_day > 0 and input_day <= 31):
    print('Winter')

elif (input_month == "February" and input_day > 0 and input_day <= 29):
    print('Winter')

elif (input_month == "March"):
    if (input_day > 0 and input_day <= 19):
        print('Winter')
    elif (input_day > 19 and input_day <= 31):
        print('Spring')
    else:
        print('Invalid')

elif (input_month == "April" and input_day > 0 and input_day <= 30):
    print('Spring')

elif (input_month == "May" and input_day > 0 and input_day <= 31):
    print('Spring')

elif (input_month == "June"):
    if (input_day > 0 and input_day <= 20):
        print('Spring')
    elif (input_day > 20 and input_day <= 30):
        print('Summer')
    else:
        print('Invalid')

elif (input_month == "July" and input_day > 0 and input_day <= 31):
    print('Summer')

elif (input_month == "August" and input_day > 0 and input_day <= 31):
    print('Summer')

elif (input_month == "September"):
    if(input_day > 0 and input_day <= 21):
        print('Summer')
    elif (input_day > 21 and input_day <= 30):
        print('Autumn')
    else:
        print('Invalid')

elif (input_month == "October" and input_day > 0 and input_day <= 31):
    print('Autumn')

elif (input_month == "November" and input_day > 0 and input_day <= 30):
    print('Autumn')

elif (input_month == "December"):
    if (input_day > 0 and input_day <= 20):
        print('Autumn')
    elif (input_day > 20 and input_day <= 31):
        print('Winter')
    else:
        print('Invalid')

else:
   print('Invalid')
