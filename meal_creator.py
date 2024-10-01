import random
import tkinter as tk
from tkinter import messagebox

def get_meal_type():
    meal_type = meal_type_var.get().strip().lower()
    return meal_type

def create_meal(meal_combinations):
    meal_choice = random.choice(meal_combinations)
    return meal_choice

def show_meal():
    meal_type = get_meal_type()
    
    if meal_type in meals:
        meal_combinations = meals[meal_type]
        meal = create_meal(meal_combinations)
        
        protein = meal['protein']
        carb = meal['carb']
        fat = meal['fat']
        
        total_protein = sum(m['protein_macros'] for m in meal_combinations)
        total_carb = sum(m['carb_macros'] for m in meal_combinations)
        total_fat = sum(m['fat_macros'] for m in meal_combinations)
        
        messagebox.showinfo("Meal Suggestion", f"Your {meal_type} to prepare consists of:\n\n"
                                               f"Protein: {protein}\nCarb: {carb}\nFat: {fat}\n\n"
                                               f"Total Macros:\nProtein: {total_protein}g\nCarb: {total_carb}g\nFat: {total_fat}g")
    else:
        messagebox.showerror("Error", "Invalid meal type entered. Please select 'breakfast', 'lunch', or 'dinner'.")

meals = {
    'breakfast': [
        {'protein': 'Eggs', 'carb': 'Toast', 'fat': 'Butter', 'protein_macros': 12, 'carb_macros': 15, 'fat_macros': 10},
        {'protein': 'Yogurt', 'carb': 'Granola', 'fat': 'Nuts', 'protein_macros': 8, 'carb_macros': 30, 'fat_macros': 12},
        {'protein': 'Bacon', 'carb': 'Pancakes', 'fat': 'Maple syrup', 'protein_macros': 10, 'carb_macros': 40, 'fat_macros': 20},
        {'protein': 'Ham', 'carb': 'Bagels', 'fat': 'Cream cheese', 'protein_macros': 14, 'carb_macros': 50, 'fat_macros': 18},
        {'protein': 'Cottage cheese', 'carb': 'Oatmeal', 'fat': 'Peanut butter', 'protein_macros': 11, 'carb_macros': 27, 'fat_macros': 16}
    ],
    'lunch': [
        {'protein': 'Chicken', 'carb': 'Rice', 'fat': 'Olive oil', 'protein_macros': 22, 'carb_macros': 35, 'fat_macros': 14},
        {'protein': 'Turkey', 'carb': 'Pasta', 'fat': 'Cheese', 'protein_macros': 19, 'carb_macros': 40, 'fat_macros': 18},
        {'protein': 'Tuna', 'carb': 'Quinoa', 'fat': 'Hummus', 'protein_macros': 24, 'carb_macros': 30, 'fat_macros': 12},
        {'protein': 'Beef', 'carb': 'Bread', 'fat': 'Guacamole', 'protein_macros': 20, 'carb_macros': 28, 'fat_macros': 20}
    ],
    'dinner': [
        {'protein': 'Beef', 'carb': 'Potatoes', 'fat': 'Butter', 'protein_macros': 25, 'carb_macros': 35, 'fat_macros': 14},
        {'protein': 'Salmon', 'carb': 'Sweet potatoes', 'fat': 'Avocado', 'protein_macros': 23, 'carb_macros': 30, 'fat_macros': 20},
        {'protein': 'Pork', 'carb': 'Noodles', 'fat': 'Olives', 'protein_macros': 20, 'carb_macros': 40, 'fat_macros': 15},
        {'protein': 'Shrimp', 'carb': 'Corn', 'fat': 'Olive oil', 'protein_macros': 18, 'carb_macros': 25, 'fat_macros': 14},
        {'protein': 'Beans', 'carb': 'Rice', 'fat': 'Cheese', 'protein_macros': 15, 'carb_macros': 35, 'fat_macros': 12}
    ]
}

# Create the main window
root = tk.Tk()
root.title("Meal Suggestion App")

# Meal type variable
meal_type_var = tk.StringVar()

# Label and dropdown for meal type selection
tk.Label(root, text="Select the meal type:").pack(pady=10)
meal_type_dropdown = tk.OptionMenu(root, meal_type_var, 'breakfast', 'lunch', 'dinner')
meal_type_dropdown.pack(pady=10)

# Button to generate meal
generate_button = tk.Button(root, text="Get Meal Suggestion", command=show_meal)
generate_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()



