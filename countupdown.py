def counter(start,stop):
    x = start
    return_string = "Counting up: "
    while x <= stop:
        return_string += str(x)
        if stop != x:
            return_string += ", "
        x += 1
    return return_string

print(counter(1,3))