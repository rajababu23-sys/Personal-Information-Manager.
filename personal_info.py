# MATTA RAJABABU - Project: Personal Information Manager
# My First Python Project
print("=" * 40)
print("     PERSONAL INFORMATION MANAGER")
print("=" * 40)

# Store static information
name = str("Matta Rajababu")
age = int(24)
city = "Visakhapatnam"
hobby = "Playing Kabaddi"

# Get user input
print("Please tell me about yourself:")
print("-"* 30)
favorite_food = input("What's your favourite food?")
while favorite_food == "":
    print("Please enter valid food!")
    favorite_food = input("What's your favorite food?")

favorite_color = input("What's your favourite color?")
while favorite_color == "":
    print("Please enter valid color!")
    favorite_color = input("What's your favorite color?")

#Calculate age in months
age_in_months = age * 12

# Display information
print()
print("=" * 40)
print("            YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye Message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)
exit()