speed_limit = 100
difference = speed - speed_limit
speed = int(input("How fast were you driving?: "))
driver = input("What is your name?: ")
if speed <= 100:
    print("Good job {}, you are not speeding.".format(driver))
elif speed > 100 and speed <150:
    charge = 10 * (difference)
    from datetime import date
    today = date.today()      
    print("{}, you are charged ${} for speeding {}km/h over the limit.".format(driver, charge, difference))
    print("Here is your receipt.")
    print("{}. {} has sped {}km/h over the limit and is charged ${:.2f}".format(today, driver, difference, charge))    
elif speed >= 150 and speed <=180:
    print("{}, you have sped {}km/h over the limit. May I see your license? Sike, it's mine now! Go back to driving school!".format(driver, difference))
elif speed > 180 and speed <=200:
    print("{}, you have sped {}km/h over the limit. You are under arrest and sentenced to 6 months in jail. Have fun talking to Jake Paul!".format(driver, difference))

else:
    print("{} has been shot by police for speeding {}km/h over the limit.".format(name, difference))
