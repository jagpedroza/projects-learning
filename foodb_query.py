import requests

def get_food_info(food_name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food_name}&page_size=1&json=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['products']:
            return data['products'][0]
        else:
            print(f"No information found for {food_name}.")
            return None
    else:
        print("Error: Unable to fetch food information.")
        return None

if __name__ == "__main__":
    food_name = input("Enter a food name to search: ")
    food_info = get_food_info(food_name)

    if food_info:
        print(f"Information for {food_name}:")
        if 'product_name' in food_info:
            print(f"Name: {food_info['product_name']}")
        if 'categories' in food_info:
            print(f"Categories: {food_info['categories']}")
        if 'nutriments' in food_info:
            print("Nutrients:")
            for nutrient, value in food_info['nutriments'].items():
                print(f"{nutrient}: {value}")
    else:
        print(f"No information found for {food_name}.")
