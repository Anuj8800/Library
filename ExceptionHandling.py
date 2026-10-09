"""
Write a function safe_divide(a, b) that:
1. Returns a divided by b.
2. Catches ZeroDivisionError and prints a clear message of your own.
3. Catches TypeError separately and prints a different message.
4. Has a finally block that prints Done every single time.

Then call the function THREE times and show the output of each:
   safe_divide(10, 2)
   safe_divide(10, 0)
   safe_divide(10, "two")

Marks: function works normally (4), ZeroDivisionError handled (5), TypeError handled separately (5), finally block (3), all three calls shown with output (3).

"""

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both arguments must be numbers.")
    finally:
        print("Done.")

# Test case
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "two")  