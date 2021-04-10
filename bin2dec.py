#This program takes in a binary number (in base 2) and outputs its decimal counterpart.
#Furthermore, it also outputs the binary numbers' bit size, byte size, and maximum possible combinations

base = 2 #binary is in base 2
nonBinaryNums = (2,3,4,5,6,7,8,9) #integers not allowed in base 2
binarySum = 0 #starting sum of binary decimal representation 

class Error(Exception):
  """Base class for all exceptions."""
  pass
class NonBinaryError(Error):
  """Raised when user inputs non-binary integers.)"""
  pass

#exception handling to ensure user input is valid
while True:
  try:
    userBinary = str(input("Enter your binary number: \n"))
    for char in userBinary:
      if int(char) in nonBinaryNums:
        raise NonBinaryError
    break 
  except NonBinaryError: #if user inputs non-binary integers
    print("Error: Only Binary numbers are accepted. Please enter 0\'s and/or 1\'s \n")
  except ValueError: #if user inputs non-numerical characters
    print("Error: Only Binary numbers are accepted. Please enter 0\'s and/or 1\'s \n")

#get num of bits for binary 
binaryBits = len(userBinary)

#for each binary digit that is 1, summate its respective placeholder value
for digit in userBinary:
  if int(digit) == 1:
    binarySum = binarySum + (base**(binaryBits-1))
    binaryBits -= 1
  else: #if digit is 0 
    binaryBits -= 1
    continue
    
print("\nDecimal value of", userBinary, "is:", binarySum)

#get total bits for binary
totalBinaryBits = int(len(userBinary))
#calculate total bytes using bits
totalBinaryBytes = float(totalBinaryBits/8)

#using recursion to find maximum combinations of bits
def getMaxCombinations(bits):
  if bits == 1:
    return 2
  else:
    return 2*getMaxCombinations(bits-1)

#calling function and assignment return value (max bit combinations) to variable
totalCombinations = getMaxCombinations(totalBinaryBits)

print("Your binary number has:", totalBinaryBits, "Bits,", totalBinaryBytes, "Bytes, and", totalCombinations, "possible combinations.\n")

#exit the program
input("press Enter or close to quit.")
