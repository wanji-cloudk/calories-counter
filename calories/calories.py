fruit_calories = {
    "Apple": 130,
    "Sweet Cherries": 100,
    "Avocado": 50,
    "Kiwifruit": 90,
    "Pear":100,
    }

def main():
    #prompts users to input a fruit
    user_input = input("Item: ").title()
    if user_input in fruit_calories:
        print(f"Calories: {fruit_calories[user_input]}")
    else:
        None

main()
