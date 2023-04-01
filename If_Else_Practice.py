# Ashton Wood
# 03-31-2023
# Small Green Sorter
# Sorts the four things as either small or green, can be both: cherry, pea, watermelon, & pumpkin

print("Enter true or false, an invalid input will be treated as false")
# Get user input for small and green
small = input("Is it Small: ")
green = input("Is it Green: ")

# Convert user input to boolean values
small = bool(small.lower() == "true")
green = bool(green.lower() == "true")

# Check which fruits match the criteria
if small and not green:
    print("The cherry is small but not green")
elif small and green:
    print("The pea is small and green")
elif not small and green:
    print("The watermelon is not small but is green")
elif not small and not green:
    print("The pumpkin is neither small nor green")
else:
    print("Enter true or false")