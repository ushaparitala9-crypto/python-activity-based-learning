## Problem Statement
The Progressive Scholarship Allocation System is designed to determine the scholarship percentage for students based on their academic marks and family annual income.
The system accepts the student's name, percentage of marks, and annual family income. Based on these details, it calculates the scholarship amount according to predefined conditions.

## Objectives
1. To identify eligible students for scholarships.
2. To calculate scholarship percentages based on marks.
3. To consider family annual income.
4. To use conditional statements in Python.
5. To reduce manual work in scholarship allocation.
3. Assumptions
1. Student marks are entered as a percentage.
2. Family income is entered in Indian Rupees.
3. Marks must be between 0 and 100.
4. Income must be a positive value.
5. Only students satisfying both conditions are eligible.
   
## Scholarship rules:
Marks	Annual family income	Scholarship
90% or above	Up to ₹2,00,000	100%
80% or above	Up to ₹3,00,000	75%
70% or above	Up to ₹5,00,000	50%
Other cases	Any	Not eligible

## Algorithm
1. Start the program.
2. Enter the student's name.
3. Enter the percentage of marks.
4. Enter the annual family income.
5. Check whether marks are 90 or above and income is up to ₹2,00,000.
6. If true, allocate a 100% scholarship.
7. Otherwise, check whether marks are 80 or above and income is up to ₹3,00,000.
8. If true, allocate a 75% scholarship.
9. Otherwise, check whether marks are 70 or above and income is up to ₹5,00,000.
10. If true, allocate a 50% scholarship.
11. Otherwise, display not eligible.
12. Stop the program.
    
## Pseudocode
START

INPUT student_name
INPUT marks
INPUT income

PRINT student_name

IF marks >= 90 AND income <= 200000 THEN
    PRINT "Scholarship: 100%"
    PRINT "Eligible"

ELSE IF marks >= 80 AND income <= 300000 THEN
    PRINT "Scholarship: 75%"
    PRINT "Eligible"

ELSE IF marks >= 70 AND income <= 500000 THEN
    PRINT "Scholarship: 50%"
    PRINT "Eligible"

ELSE
    PRINT "Scholarship: Not Available"
    PRINT "Not Eligible"

END IF

STOP

## Test Cases
Test | Student | Marks	| Annual income  |	Expected result
1    |	Ravi	 |  95    |	 ₹1,50,000     |	100%
2	   |  Sita   |	85	  |  ₹2,50,000     |	75%
3    |	Kumar  |	75	  |  ₹4,00,000     |	50%
4	   |  Rani   |	65    |	 ₹1,00,000	   | Not eligible
5	   |  Arun	 |  95	  |  ₹3,00,000     | Not eligible

## Sample Input and Outputs
case1:
Enter student name: Ravi
Enter percentage of marks: 95
Enter family annual income: 150000

--- Scholarship Details ---
Student Name: Ravi
Scholarship: 100%
Status: Eligible

case2:
Enter student name: Sita
Enter percentage of marks: 85
Enter family annual income: 250000

--- Scholarship Details ---
Student Name: Sita
Scholarship: 75%
Status: Eligible

case3:
Enter student name: Kumar
Enter percentage of marks: 75
Enter family annual income: 400000

--- Scholarship Details ---
Student Name: Kumar
Scholarship: 50%
Status: Eligible

## Flowchart
```mermaid
graph TD
    A([Start]) --> B[/Input/]
    B --> C{Condition?}
    C -- Yes --> D[Process]
    C -- No --> E[Process]
    D --> F[/Output/]
    E --> F
    F --> G([Stop])
  ```
