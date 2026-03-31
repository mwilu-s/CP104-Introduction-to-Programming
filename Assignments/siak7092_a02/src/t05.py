"""
-------------------------------------------------------
[program description]
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

lengthF = float(input("Foundation length (m): "))
widthF = float(input("Foundation width (m): "))
heightF = float(input("Foundation height (m): "))
wallHeight = float(input("Wall height (m): "))
costConcrete = float(input("Cost of concrete ($/m^3): "))
costBricks = float(input("Cost of bricks ($/m^2): "))

concreteF = lengthF * widthF * heightF
totalCostC = concreteF * costConcrete
wallBricks = 2*(lengthF * wallHeight) + 2*(widthF * wallHeight)
totalCostB = wallBricks * costBricks
total = totalCostB + totalCostC

print(f"""Concrete needed for foundation (m^3): {concreteF:.2f}
Cost of concrete: ${totalCostC:,.2f}
Bricks needed for walls (m^2): {wallBricks: .2f}
Cost of bricks: ${totalCostB:,.2f}
Total cost: ${total:,.2f}
""")