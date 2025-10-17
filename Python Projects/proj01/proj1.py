#This program converts distance (entered in rods)
#into meters, feet, miles, furlongs, and walking time (in minutes).

#prompt for user input
rods = float(input("Enter distance in rods: "))

#Conversation constants
ROD_TO_METERS = 5.0292
METER_TO_FEET = 1/0.3048
METER_TO_MILES = 1/1609.34
ROD_TO_FURLONG = 1/40
WALKING_SPEED_MPH = 3.1   #MPH - miles per hour

#Perform conversations
meters = rods * ROD_TO_METERS
feet = meters * METER_TO_FEET
miles = meters * METER_TO_MILES
furlongs = rods * ROD_TO_FURLONG
time_minutes = (miles / WALKING_SPEED_MPH) * 60

#Display results
print("\nDistance in various units:")
print(f"Rods:{rods:.3f}")
print(f"Feet:{feet:.3f}")
print(f"Miles:{miles:.5f}")
print(f"Furlongs:{furlongs:.3f}")
print(f"Time to walk:{rods:.3f} rods: {time_minutes:.2f} minutes    ")