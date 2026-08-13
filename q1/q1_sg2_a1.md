9-Samat
#25, #26, #27
MERGILLANO, PANGILINAN, SADORRA

ANNEX A: Smart School Canteen Queue

Main problem:
Many students endure long queues and lines to buy food from the school canteen to ease their cravings or hunger. But from time to time, food stock in the canteen may run out unexpectedly, disappointing a lot of students and causes queues to slow down. This happens due to the fact that there is no system or person in charge to keep track of the availability and amount of food stock.

Subproblems:
1. No specific system to input or track food items and their amount.
   - CT Skill: Algorithim
   - Example solution: Create a system to help canteen vendors track food items and its remaining amount.

2. No specific system to update students or staff every time a food item is bought or used.
   - CT Skill: Algorithim
   - Example solution: Create a system to update customers when a specific food item is bought or used.

3. No specific system to alert or notify the canteen vendor to stock up on a food item.
   - CT Skill: Algorithim
   - Example solution: Create a system where it notifies the canteen vendor to refill or stock up on a specific food item.

Pseudocodes:

Subproblem #1:

BEGIN
  OUTPUT "Enter the food item name: "
  INPUT food_item

  OUTPUT "Enter the amount: "
  INPUT item_amount
END


Subproblem #2:
1. Begin program
2. Input the food items that are being sold in the canteen and their amount in a list
3. Create an IF Statement asking if a certain food item was bought/used or not (Y/N)
4. IF a specific food item in the list was bought/used:
   - Create an input asking how many of a certain food item was bought/used
   - Update customers about the new amount
6. ELIF a specific food item in the list was not bought/used, end the program (leave the amount unchanged)
7. End program


Subproblem #3

1. Begin program
2. Input the food items that are being sold in the canteen and their amount in a list
3. Create an IF Statement regarding the amount of a certain food item in the list
4. IF a specific food item's amount in the list is == 0, then alert the canteen vendor to restock that item
5. ELIF a specific food item's amount in the list is > 0, end the program
6. End program
