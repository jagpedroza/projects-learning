import requests

def get_food_info(food_name):
    url = f"https://foodb.ca/api/v1/foods/search?q={food_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch food information.")
        return None

def suggest_meals(diet_components):
    for component, amount in diet_components.items():
        print(f"Suggestions for {component}:")
        if component.lower() == 'bone meat':
            print("Meals containing raw chicken necks, raw beef ribs, etc.")
        elif component.lower() == 'meat and fish':
            print("Meals containing lean meats like chicken, turkey, beef, or fish.")
        elif component.lower() == 'organs and viscera':
            print("Meals containing liver, kidney, or other organ meats.")
        elif component.lower() == 'vegetables':
            print("Meals containing dog-safe vegetables like carrots, spinach, or broccoli.")
        elif component.lower() == 'fruit':
            print("Meals containing dog-safe fruits like apple slices or blueberries.")
        else:
            print("No specific meal suggestions available.")

def calculate_barf():
    print("Select the age group of the dog:")
    print("a - Dog is younger than 12 months")
    print("b - Dog is older than 12 months")
    
    age = input("Enter the corresponding letter: ").lower()
    
    if age == 'a':
        activity_factor = get_activity_factor_puppy()
    elif age == 'b':
        activity_factor = get_activity_factor_adult()
    else:
        print('Please enter "a" or "b".')
        return

    frequency_factor = get_frequency_factor()
    weight = float(input("Enter the dog's ideal weight in kilograms: "))
    diet_components = calculate_diet_components(weight, activity_factor, frequency_factor)
    display_results(diet_components)

    suggest_meals(diet_components)

def get_activity_factor_puppy():
    print("Select puppy activity level:")
    print("a - 2-4 months")
    print("b - 5-6 months")
    print("c - 7-8 months")
    print("d - 9-10 months")
    print("e - 11-12 months")
    
    activity = input('Enter the corresponding letter: ').lower()
    activity_factors = {'a': 0.1, 'b': 0.08, 'c': 0.06, 'd': 0.04, 'e': 0.03}
    return activity_factors.get(activity, 0.03)

def get_activity_factor_adult():
    print("Select adult dog activity level:")
    print("a - Sedentary or sterilized")
    print("b - Normal")
    print("c - Athlete")
    
    activity = input('Enter the corresponding letter: ').lower()
    activity_factors = {'a': 0.02, 'b': 0.025, 'c': 0.03}
    return activity_factors.get(activity, 0.025)

def get_frequency_factor():
    print("Select feeding frequency:")
    print("a - Daily")
    print("b - Weekly")
    print("c - Bi-weekly")
    print("d - Monthly")
    
    frequency = input('Enter the corresponding letter: ').lower()
    frequency_factors = {'a': 1, 'b': 7, 'c': 15, 'd': 30}
    return frequency_factors.get(frequency, 30)

def calculate_diet_components(weight, activity_factor, frequency_factor):
    hc = weight * activity_factor * frequency_factor * 0.5
    cp = weight * activity_factor * frequency_factor * 0.3
    vo = weight * activity_factor * frequency_factor * 0.1
    vv = weight * activity_factor * frequency_factor * 0.06
    ft = weight * activity_factor * frequency_factor * 0.04
    return {'Bone meat': hc, 'Meat and fish': cp, 'Organs and viscera': vo,
            'Vegetables': vv, 'Fruit': ft}

def display_results(diet_components):
    print('The dog should eat:')
    for component, amount in diet_components.items():
        print(f'{component}: {amount:.2f} Kilograms')

if __name__ == "__main__":
    calculate_barf()
