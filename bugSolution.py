def function_with_uncommon_error(x):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        else:
            return 10/x
    except ZeroDivisionError as e:
        print("Error:", e)
        return None

result = function_with_uncommon_error(0)
print(result)

result2 = function_with_uncommon_error(5)
print(result2)