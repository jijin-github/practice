# Example: globals() function
x = 9


def fn():
    y = 3
    z = y + x
    # Calling the globals() method
    z = globals()['x'] = z
    return z


# Test Code
ret = fn()
print(ret)