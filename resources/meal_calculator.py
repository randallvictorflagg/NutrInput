from models.food import FoodModel
import json

def meal_calculator(meal_template):
    #meal_template.composition = eval(meal_template.composition)
    nutrient_attributes = [ "calories", "carbohydrate", "protein", "total_fat", "saturated_fat", "polyunsaturated_fat", "monounsaturated_fat", "trans_fat",\
                                       "cholesterol", "sodium", "fiber", "sugar", "vitamin_a", "vitamin_b1", "vitamin_b12", "vitamin_c", "vitamin_d", "vitamin_e", "vitamin_k", "potassium", "zync", "magnesium", "iron", "chromium"]
    for attribute in nutrient_attributes:
        setattr(meal_template, attribute,0)
    for index in meal_template.composition:
        if "food_id" not in index or "food_amount" not in index:
            return "One or more fields in food composition is missing."
        food = FoodModel.find_food(index["food_id"])
        if food:
            if (food.serving_amount is None):
                food.serving_amount = 0 
            try:
                for attribute in nutrient_attributes:
                    meal_template_value = getattr(meal_template, attribute, 0)
                    food_value = getattr(food, attribute, 0.0)
                    food_amount = float(index["food_amount"])
                    serving_amount = float(food.serving_amount)
                    setattr(meal_template, attribute, (meal_template_value + (food_value * food_amount) / serving_amount))
            except Exception as e:
                print(e)
                return "Error calculating meal nutritional value."
        else:
            return "Food not found."
    return meal_template

   