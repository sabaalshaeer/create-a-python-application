"""This program counts the number of times each unique word appears
in a text file. the results are output to the command line and the
user is given the option of printing the result to a new file ."""

user_input = input("Please enter the path and name of the text file you want"
                   " to analyze. ( E.G., C:/Users/Yourname/Desktop/File.txt):"
                   "\n")

# Sending user's input back to them,for now.
print(user_input)

common_word = input("would you like to strip common words from the results? (Y/N) ")

print(common_word)

user_output = input("\nWould you like to output these results to a file? (Y/N) ")

print(user_output)