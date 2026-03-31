"""
-------------------------------------------------------
Meals
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-27"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """

breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
dinner = float(input("Enter cost of dinner: $"))
totalCost = breakfast + lunch + dinner



print(f"""{"Meal":17s} Cost
{"Breakfast":17s} ${breakfast:6.2f}
{"Lunch":17s} ${lunch:6.2f}
{"Dinner":17s} ${dinner:6.2f}
{"Total":17s} ${totalCost:6.2f}

""")