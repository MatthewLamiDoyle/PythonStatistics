"""
Program: DoyleU6AE.py
Author: Matthew Doyle
Last Date Modified: 02/21/2022
Version 2: Added a try/except loop for the input file name to avoid exception
The purpose of this program is to demostrate the use of the Python functions to complete statistical analysis on an external file containing numbers.
"""
# The algorithm that this program will use is as follows:
# Assign the user a username and welcome them
# Ask the user if they need instructions
# If they need instructions, display them
# Define the mathematical and statistical functions necessary for analysis
# Ask the user to input the file name for analysis
# Properly open and run statistical analysis on their file
# Display the statistics for the user
# Ask the user if they would like to analyze another file
# If they do, repeat the file name input and analysis process
# Otherwise display a closing message and exit.

# ----Begin Code----

def main():
  # The main function for this script.
  print ("Descriptive Statistics App running")

if __name__ == "__main__":
  main()


# Assign a username and welcome the user.

Username = input ("What is your name?: ")

print (f"Welcome {Username} this program will provide descriptive statistics on values contained in other files. ")

# Ask if the user would like to see the instructions

instructions = input ("Would you like to review the instructions? (Y/N): ")

# If the user inputs "Y" display the instructions

if instructions == 'Y':
  print("     To run descriptive statistics on your data you must input the file name into this program when prompted.")
  print("     Be aware that the file name is case sensitive.")
  print("     After running analysis, to analyze another file answer Y when prompted and input another file name.")

  # Input to continue after the instructions are displayed

  input("When you are ready to begin press enter:")

myValues = []

def myMean(myValues): 
  # This function expects a list of values and returns the statistical average of them.
  sum = 0.0
  for i in range (len(myValues)):
    sum += myValues[i]
  return sum/len(myValues)

def myMedian(myValues): 
  # Sort the list, if even add the middle numbers and divide by two, if odd simply return the middle value.
  myValues = sorted(myValues)
  if len(myValues) % 2 == 0:
    return (myValues[len(myValues) // 2] + myValues[(len(myValues) - 1) // 2]) / 2
  else:
    return myValues[len(myValues) // 2]
  

def myMode(myValues):
  modeDict = {}
  modeList = []
  for n in myValues: # Begin a loop
    modeDict.setdefault(n,0) # Set every number in the dictionary to a default value of 0.
    modeDict[n] += 1 # For every number in the list add 1 to the default value of the number in the dictionary.
  f = max(modeDict.values()) # Check for the highest value in the dictionary.
  for n, i in modeDict.items(): # Begin a loop of the dictionary.
    if i == f: # If a dictionary key has a value equal to the max value add it to a list of modes.
      modeList.append(n)
    modeList.sort() # Sort the new list of modes for readability.
  return modeList
  
def mySumOfSquares(myValues):
  i = myMean(myValues) # Define a mean variable.
  sumSquares = sum((n - i) ** 2 for n in myValues) # Subtract the mean from each of the values in the list, square each of the new values, and then add them all up.
  return sumSquares

def myVar(myValues):
  n = len(myValues) 
  sumSquares = mySumOfSquares(myValues)
  v = sumSquares / (n-1) # Divide the sum of squares by the count of variables in the list minus one.
  return v

def myStdDev(myValues):
  # To find the std dev simply calculate the sqr rt of the variance.
  stdDev = myVar(myValues) ** 0.5
  return stdDev

def myMax(myValues):
  # Starting at n = 0 loop through the list replacing n if the value is greater than the previous value until the loop ends, then return the value of n.
  n = myValues[0]
  for i in myValues:
    if i > n:
       n = i
  return n  

def myMin(myValues):
   # Starting at n = 0 loop through the list replacing n if the value is less than the previous value until the loop ends, then return the value of n.
  n = myValues[0]
  for i in myValues:
    if i < n:
       n = i
  return n

def myRange(myValues):
  # To find the range simply subtract the minimum value from the maximum value.
  x = myMax(myValues)
  n = myMin(myValues)
  return x - n

def mySum(myValues):
  # To find the sum of values use a for loop to add every value in the list starting at 0.
  i = 0
  for n in myValues:
    i += n
  return i

def myCount(myValues):
  # To find the count simply loop through the list adding 1 to i for each value in the list.
  i = 0
  for n in myValues:
    i = i + 1
  return i

# Input the file name to be opened and analyzed

infileName = 0

while (infileName != '1'):

  infileName = input("Enter the name of the data file to be analyzed: ")

  # Test to see if the input file name exists.

  while 1 == 1: # Loop the test incase of multiple wrong inputs.
    try:
      f = open(infileName, 'r')
      break # End the loop if the file exists.
    except:
      print(f"No file named '{infileName}' was found, please try again.")
      infileName = input("Enter the name of the data file to be analyzed: ")

  # Read the data file provided by the user

  f = open(infileName, 'r')

  # An empty list

  myValues = []
  
  for line in f: 
    value = line.strip()
    number = int(value)
    myValues.append(number)


  print("")
  
  print ("%-20s" % "Measure", "%10s" % "Results")

  print ("--------------------------------------------------")

  print("%-20s" % "Mean:", "%10.2f" % myMean(myValues))

  print("%-20s" % "Median:", "%10.2f" % myMedian(myValues))

  print("%-20s" % "Mode:" f"                    {myMode(myValues)}")

  print("%-20s" % "Std Dev (Sample):", "%10.2f" % myStdDev(myValues))

  print("%-20s" % "Variance (Sample):", "%10.2f" % myVar(myValues))

  print("%-20s" % "Minimum:", "%10.2f" % myMin(myValues))

  print("%-20s" % "Maximum:", "%10.2f" % myMax(myValues))

  print("%-20s" % "Range:", "%10.2f" % myRange(myValues))

  print("%-20s" % "Sum:", "%10.2f" % mySum(myValues))

  print("%-20s" % "Count:", "%10.2f" % myCount(myValues))

  print("")

  # Give the user a choice to analyze another file.

  choice = input("Would you like to analyze another file? (Y/N)")

  # If the user inputs Y, continue the loop, otherwise the program will exit.
  if choice != 'Y':
    print ("Thank you for using the Descriptive Statistics App, it will now exit.")
    break