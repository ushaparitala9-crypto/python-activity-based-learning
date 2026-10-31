## Problem Statement
Develop a Python program to calculate the electricity bill of a customer based on the number of electricity units consumed. The program should accept the customer's name and electricity units as input and calculate the total bill using a progressive billing system.

The electricity charges are calculated according to the following rates:
Electricity units	Rate per unit
First 100 units	₹2
101–200 units	₹3
201–300 units	₹5
Above 300 units	₹7&nbsp;

The program should display the customer's name, units consumed, and total electricity bill.

## Objectives
1. To understand conditional statements in Python.
2. To calculate electricity bills using progressive rates.
3. To understand the use of if, elif, and else.
4. To accept customer details using input functions.
5. To display the final electricity bill accurately.
 
## Assumptions
1. The customer name is entered as a string.
2. Electricity units are entered as a positive integer.
3. The first 100 units cost ₹2 per unit.
4. The next 100 units cost ₹3 per unit.
5. The next 100 units cost ₹5 per unit.
6. Units above 300 cost ₹7 per unit.
7. There are no additional taxes or fixed charges.
 
## Algorithm
1. Start the program.
2. Read the customer's name.
3. Read the electricity units consumed.
4. Check the number of units:
   - If units are less than or equal to 100, multiply by 2.
   - If units are between 101 and 200, calculate the first 100 units at ₹2 and remaining units at ₹3.
   - If units are between 201 and 300, calculate the first 100 units at ₹2, next 100 at ₹3, and remaining units at ₹5.
   - If units are above 300, calculate the first 300 units according to their rates and remaining units at ₹7.
6. Display the customer's name.
7. Display the units consumed.
8. Display the total electricity bill.
9. Stop the program.

## Pseudocode
START

INPUT customer_name
INPUT units

IF units <= 100 THEN
    bill = units * 2

ELSE IF units <= 200 THEN
    bill = (100 * 2) + (units - 100) * 3

ELSE IF units <= 300 THEN
    bill = (100 * 2) + (100 * 3)
           + (units - 200) * 5

ELSE
    bill = (100 * 2) + (100 * 3)
           + (100 * 5) + (units - 300) * 7

END IF

PRINT customer_name
PRINT units
PRINT bill

STOP

## Test Cases
The following test cases are used to check whether the program produces correct results.
```
Testcase |	Units consumed  |	Expected bill
   1     |     	 50	        |    ₹100
   2	   |      100         |  	 ₹200
   3	   |      150	        |    ₹350
   4	   |      200	        |    ₹500
   5     |    	250	        |    ₹750
   6	   |      300	        |    ₹1,000
   7	   |      400	        |    ₹1,700
```
## Sample Output Screenshots
Enter customer name: Usha
Enter electricity units consumed: 150

--- Electricity Bill ---
Customer Name: Usha
Units Consumed: 150
Total Electricity Bill: Rs. 350
Enter customer name: Usha
Enter electricity units consumed: 400

--- Electricity Bill ---
Customer Name: Usha
Units Consumed: 400
Total Electricity Bill: Rs. 1700

## Conclusion
This case study explains how Python can be used to calculate electricity bills using a progressive billing system. The program uses conditional statements such as if, elif, and else to calculate charges based on electricity consumption. It helps beginners understand decision-making statements, user input, arithmetic operations, and output statements in Python. The program calculates the electricity bill accurately for different ranges of units consumed.

## Flowchart
```mermaid
graph TD
    A([Start]) --> B[/Input/]
    B --> C{Condition?}
    C -->|Yes| D[Process]
    C -->|No| E[Process]
    D --> F[/Output/]
    E --> F
    F --> G([Stop])
    ```
