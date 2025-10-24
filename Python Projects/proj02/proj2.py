# Project 02: Earthquake Energy Calculator
# This program calculates and displays the amount of energy 
# released by an earyhquake based on its magnitude 
# on the Richer scale. The energy is shown both in: 
#  1. Joules
#  2. Tons of TNT eqivalent

# Function calculates energy based on Richer mangnitude
def calculate_energy(richter):
    """
    Calculate the energy released during earthquake
    Formula:
        Energy (in Joules) = 10 ** ((1.5 * Richter) + 4.8)
    Conversation:
        1 ton of TNT = 4.184 * 10^9 joules 
    """ 

    #Calculate energy in joules using richter formula
    energy_joules = 10 ** ((1.5 * richter) + 4.8)

    #Convert joules to tons of TNT
    energy_tnt = energy_joules / 4.184e9

    #return both the values
    return energy_joules, energy_tnt

# Function to display formatted energy results
def display_energy(richter):
    """
    Display the calculated energy values for richter magnitude.
    """ 
    energy_joules, energy_tnt = calculate_energy(richter)
    print(f"\nRichter scale value: {richter}")
    print(f"Energy released: {energy_joules:.2e} joules")
    print(f"Equivalent to: {energy_tnt:.2e} tons of TNT")

#--------------------------------------------------------
# Main program
#--------------------------------------------------------

#step 1: display predefined earthquake data for reference
print("=============================================")
print("   EARTHQUAKE ENERGY CALCULATOR  ")
print("==============================================")
print("Below some are known earthquake magnitudes:\n")

#loop through predefined Richter scale values and show results
for value in [1.0,5.0,9.1,9.2,9.5]:
    display_energy(value)

#step 2: prompt user to enter their own richter scale values
try:
    user_input= float(input("\nEnter a richter scale value to calculate energy: "))
    display_energy(user_input)

# Handle invalid input (e.g., letters instead of numbers)
except ValueError:
    print("\nInvalid input! Please enter a valid numeric value.")