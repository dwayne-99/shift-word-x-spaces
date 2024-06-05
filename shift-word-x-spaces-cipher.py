def shift_x_spaces(word, shift_by):
  
  shifted_word = ""
  # Initialize an empty string to store the shifted word
  
  if shift_by < 0:
    shift_by = len(word) - (-shift_by % len(word))

  # If shift_by is negative, shift in the opposite direction
  # In essence, this code reinterprets a negative shift_by value as a positive offset from the end of the word,
  # enabling left shifts for negative shift amounts
  
  for i in range(len(word)):
    shifted_index = (i + shift_by) % len(word)
    shifted_word += word[shifted_index]
  print(shifted_word)

  # loop through each character in the word
  # Calculate the shifted index by adding shift_by to the current index i
  # and taking the modulo with the word length to wrap around if necessary
  # Add the shifted character to the shifted_word string

encrypt = input("type encode to encrypt ")

word = input("Enter a word ")
shift_by = int(input("Enter the number of spaces to shift "))

if encrypt == ("encode"):
  shift_x_spaces(word, shift_by)

# If the user enters "encode", the program will prompt them to enter a word and the number of spaces to shift
# It will then call the shift_x_spaces function to perform the shift