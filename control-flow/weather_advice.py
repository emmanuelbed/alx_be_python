# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

user_input = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if user_input == "sunny":
    print("Wear a t-shirt and sunglasses.")
if user_input == "rainy":
    print("Don't forget your umbrella and a raincoat.")
if user_input == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")


