def function_with_uncommon_error_fixed(x):
    if x == 0:
        return 1
    elif x != 0:
        return x / x # avoids ZeroDivisionError
    else:
        return None #Handle cases not yet considered

result = function_with_uncommon_error_fixed(0)
print(result) # This will print 1
result = function_with_uncommon_error_fixed(5)
print(result) # This will print 1
result = function_with_uncommon_error_fixed(-5)
print(result) # This will print -1