"""
### **Logical Operators**

🧠 Use `and`, `or`, `not` to check:

- If a person is eligible to vote (`age >= 18`) **and** is a citizen
- If either condition fails
- Show the use of `not` operator
"""
age = 20
citizen = True

# Using AND
if age >= 18 and citizen:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#using or
if age >= 18 or citizen:
    print("Partially eligible")
else:
    print("Not eligible at all")

