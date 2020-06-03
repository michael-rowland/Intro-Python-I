def stupid_addition(a, b):

    a_type, b_type = type(a), type(b)
    if a_type != b_type:
        return None
    
    if a_type == str:
        # _TODO: if datatypes are strings, ensure they can be converted to int
        return int(a) + int(b)

    if a_type == int:
        return str(a) + str(b)


print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))