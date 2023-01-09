"""
Program: DoyleU5AE.py
Author: Matthew Doyle
Last Date Modified: 02/12/2022

The purpose of this program is to simulate rolling dice, outputting a visualization of the rolls, and to provide
statistics related to the outcomes. The program will demonstrate my ability to use lists, dictionaries, Python modules,
visualize data analysis, and user experience.
"""
# ----------------------------------------------------------------------------
# The algorithm that this program will follow is:
# Import necessary modules.
# Receive a username from the user.
# Welcome the user to the program.
# Offer a choice for instructions to the user.
# Display instructions to the user if they choose to see them and wait for a user input to continue, otherwise simply
# continue the program.
# Run a function to receive dice specifications from the user.
# Create a list to receive dice rolls.
# Create a dictionary for use in the visualization.
# Define a manual dice rolling function.
# Define an automatic dice rolling function.
# Give the user an input option to choose manual or automatic dice rolls.
# Execute the chosen dice rolling function, and write the outcomes to the list.
# Define a visualization function to output information about the rolls from the rolls list and by using the dictionary.
# Define a statistics function to output descriptive statistics related to the rolls list.
# Sort the rolls list from least to greatest for readability.
# Define a function to aggregate displaying the visualization, statistics, and the sorted rolls list.
# Run the aggregated outcome function to display the information to the user.
# Offer the user a choice to continue running dice rolling simulations or to exit.
# While the user choice is to continue running simulations enter a loop.
# Within the loop clear the list and dictionary to receive fresh values, and then call in order the input function, the
# manual or auto choice, and finally the aggregated output function.
# At the end of each loop offer the user the option to continue.
# If the user chooses not to continue end the loop and display an exit message
# Exit the program.
# ----------------------------------------------------------------------------

# Import randint from the random module, import the statistics module, and import sleep from the time module.

from random import randint
from time import sleep
import statistics

Username = input("Please enter your name: ")  # Assign a username and welcome the user.

# Added an f-string to my welcome message to remove the whitespace after the username.

print(
    f"Welcome {Username}, this program will simulate custom dice rolls and display descriptive statistics with a "
    f"visualization of the roll outcomes.")
print("")  # Whitespace after welcome message to separate the instructions choice.

# Ask if the user would like to see the instructions
instructions = input("Would you like to review the instructions? (Y/N): ")

if instructions == 'Y':  # If the user inputs "Y" display the instructions
    print("")
    print(
        "The program will ask you to input the number of faces or sides for your dice, the number of dice to "
        "simultaneously roll, and how many total times you would like to roll the dice.")
    print("     These values should be entered as numbers i.e. 1,2,3, etc.")
    print(
        "The program will then ask if you would like to manually roll the dice meaning that you will press enter for "
        "each roll, otherwise it will automatically complete the rolls on a timer.")
    print(
        "Once you have completed your rolls of the dice the program will output a visualization of the rolls, "
        "a list of the rolls, and statistics related to the rolls.")
    print(
        "You will then have an option to run additional simulated dice rolls or to exit the program after each "
        "simulation.")
    print("")
    input("When you are ready to continue press enter:")  # Input to continue.


def inputDice():
    global numFace, numDice, numRolls  # Define the variables in the function as global to be used in later functions.
    numFace = input("How many faces would you like your die/dice to have: ")
    numDice = input("How many dice would you like to simultaneously roll: ")
    numRolls = input("How many times would you like to roll the dice: ")

    # Convert the user input strings to integers for use in the roll functions to avoid TypeErrors.

    numFace = int(numFace)
    numDice = int(numDice)
    numRolls = int(numRolls)


inputDice()  # Run the input dice function to allow the user to specify their dice and number of rolls.

rollResults = []  # Add an empty list to receive the roll results.

diceDictionary = {}  # Add an empty dictionary for use in the visualization.


# Define a function to roll the dice manually using the interval converted user inputs.

def roll_Dice_manual(numFace, numRolls):
    for i in range(numRolls):  # Use a for loop to roll as many times as the user defined.
        roll = randint(numDice, numFace * numDice)  # Use randint to "roll" the dice
        rollResults.append(roll)  # Add the previous roll to the results list.
        print(rollResults)  # Print the roll results list each time a die is rolled.
        input("Press enter to roll again:")  # Add an input for every roll.


# Define another function to roll the dice automatically.

def roll_Dice_auto(numFace, numRolls):
    for i in range(numRolls):  # Use a for loop to roll as many times as the user defined.
        roll = randint(numDice, numFace * numDice)  # Use randint to "roll" the dice
        rollResults.append(roll)  # Add the previous roll to the results list.
        print(rollResults)  # Print the roll results list each time a die is rolled.
        sleep(1.5)  # Wait 1.5 seconds between automatic rolls.


manualChoice = input("Would you like to roll the dice manually for this simulation? (Y/N):")

if manualChoice == 'Y':
    input("Press enter to roll the dice:")
    roll_Dice_manual(numFace, numRolls)  # Run the manual dice roll function with the user input dice.

else:
    roll_Dice_auto(numFace, numRolls)  # Run the automatic dice roll function with the user input dice.


def simulationVisual():  # Define a function for generating the visualization.
    count = 0  # Set the count back to zero each time the function is called.
    print(f"| Total rolls: {numRolls} Dice Count: {numDice} Dice Faces: {numFace} | ")
    print("{:<15} {:<15} {:<25} {:<20}".format('#', 'Count', 'Percentage', 'Graph'))
    print("---------------------------------------------------------------------------------------")
    for n in rollResults:  # Start a for loop.
        if n in diceDictionary:  # Scan the dictionary for values.
            diceDictionary[n] += 1  # Look for values of rolls and then increase the count if found.
            count = count + 1
        else:
            diceDictionary[n] = 1  # Look for values of rolls and then increase the count if found.
            count = count + 1
    for i in range(numDice,
                   numFace * numDice + 1):  # Start a loop on a range with at minimum the number of dice, and then
        # the number of faces multiplied by the number of dice
        if i in diceDictionary.keys():
            visualPercent = diceDictionary[i] / numRolls * 100  # Convert the roll count value to a percentage.
            outcomeNum = str(i) + ":"  # Add the colon to the outcome numbers.
            visualCount = diceDictionary[int(i)]  # Display the total counts.

            # Format the values within the graph, add the decimal places and percent sign to the percentage values.
            print("{:<15} {:<15} {:<20}".format(outcomeNum, visualCount, str("{:.2f}".format(visualPercent)) + " %"),
                  end="")

        else:
            visualPercent = 00  # Add the decimal places to the percentage.
            outcomeNum = str(i) + ":"  # Add the colon to the outcome numbers.
            outcomePercent = " 0.00 %"  # Set the baseline value for the percentages.
            print("{:<15} {:<15} {:<20}".format(outcomeNum, visualPercent, outcomePercent), end="")

        for f in range(0, int(visualPercent) + 1):  # Count through a range of the percentage to print the graph bars.
            print("|", end="")

        print('')  # Added a whitespace to preserve formatting.

    print("---------------------------------------------------------------------------------------")
    countSum = count  # Assign a total count value.
    print("{:<15} {:<15} {:<15}".format("Sum:", countSum,
                                        "100.00 %"))  # Format the bottom row of the visual/add the total count.


def rollStatistics():  # Define a function to output statistics on the rolls.
    print("The mean of the rolls was    : ", statistics.mean(rollResults))
    print("The median of the rolls was  : ", statistics.median(rollResults))
    print("The mode of the rolls was    : ", statistics.mode(rollResults))
    print("The std dev of the rolls was : ", statistics.stdev(rollResults))
    print("The variance of the rolls was: ", statistics.variance(rollResults))
    print("The minimum of the rolls was : ", min(rollResults))
    print("The maximum of the rolls was : ", max(rollResults))
    print("The range of the rolls was   : ", max(rollResults) - min(rollResults))
    print("The sum of the rolls was     : ", sum(rollResults))
    print("The count of the rolls was   : ", len(rollResults))


def outcomeOutput():  # Define a function to easily output the results.
    print("End of rolls - Calculating results")  # Give the user an indication that rolls have ended.
    sleep(3)  # Added this to give a few seconds before results show up to make the ux smoother.
    print("")  # Added whitespaces between various outputs to increase readability.
    rollResults.sort()  # Sort the roll values for readability.
    print(f"Rolls {rollResults}")  # Print the sorted list for the user.
    print("")  # Added whitespaces between various outputs to increase readability.
    simulationVisual()  # Call the visualization function.
    print("")  # Added whitespaces between various outputs to increase readability.
    rollStatistics()  # Call the statistics function.


outcomeOutput()  # Run the aggregated output function.

print("")  # Whitespace to emphasize the choice input text.

continueChoice = input("Would you like to run another dice roll simulation? (Y/N)")

while continueChoice == 'Y':
    rollResults.clear()  # Clear the list for use in the next simulation.
    diceDictionary.clear()  # Clear the dictionary for use in the next simulation.
    inputDice()  # Call the input dice function
    # Run the manual or automatic choice.
    manualChoice = input("Would you like to roll the dice manually for this simulation? (Y/N):")

    if manualChoice == 'Y':
        input("Press enter to roll the dice:")
        roll_Dice_manual(numFace, numRolls)  # Run the manual dice roll function with the user input dice.

    else:
        roll_Dice_auto(numFace, numRolls)  # Run the automatic dice roll function with the user input dice.

    outcomeOutput()  # Run the aggregated output function.
    print("")  # Whitespace to emphasize the choice input text.
    continueChoice = input("Would you like to run another dice roll simulation? (Y/N)")

print("The application will now close, thank you for using the Dice Roll Simulator.")
