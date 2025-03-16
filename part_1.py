# 1. Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
print("\nQUESTION 1\n")
print("Name : Asjal Amir\nFather Name : Muhammad Amir\nDOB : 23 September 2004")

# 2. Write your small bio using variables and print it using print function
print("\nQUESTION 2\n")

name = "Asjal Amir"
father_name = "Muhammad Amir"
city = "Karachi"
country = "Pakistan"
dob = "23 September"

print(f"Bio Data :\n{name}\n{father_name}\n{city}\n{country}\n{dob}")

# 3. Write a program in which use all the operators we can use in Python
print("\nQUESTION 3\n")

# Arithmetic Operators
a, b = 10, 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Comparison Operators
print("\nComparison Operators:")
print(a, "==", b, ":", a == b)
print(a, "!=", b, ":", a != b)
print(a, ">", b, ":", a > b)
print(a, "<", b, ":", a < b)
print(a, ">=", b, ":", a >= b)
print(a, "<=", b, ":", a <= b)

# Logical Operators
x, y = True, False
print("\nLogical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)


# Assignment Operators
c = 10
print("\nAssignment Operators:")
c += 5
print("c += 5:", c)
c -= 2
print("c -= 2:", c)
c *= 3
print("c *= 3:", c)
c /= 2
print("c /= 2:", c)


print("\nQUESTION 4\n")

# 4. Completes the following steps of small task:

    # Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
    # Mention Variable of Total Marks and assign 300 to it
    # Calculate Percentage

# Step 1 : 
english_marks = 82
islamiat_marks = 83
maths_marks = 85

# Step 2: 
total_marks = 300

# Step 3: 
obtained_marks = english_marks + islamiat_marks + maths_marks
percentage = (obtained_marks / total_marks) * 100

print("Marks Obtained:", obtained_marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")

