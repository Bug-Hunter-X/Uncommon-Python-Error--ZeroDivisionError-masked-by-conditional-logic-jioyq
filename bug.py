def function_with_uncommon_error(x):
    if x == 0:
        return 1
    else:
        return x / 0  # ZeroDivisionError

result = function_with_uncommon_error(0)
print(result) # This will print 1
result = function_with_uncommon_error(5)
print(result) # This will raise ZeroDivisionError