
first_arg ="Monty"
second_arg =3

def string_compare (first_arg, second_arg):

    if type(first_arg) == str and type(second_arg) == str:
        if first_arg == second_arg:
            return  1
        elif len(first_arg) > len(second_arg):   
            return 2
        elif second_arg == "learn":
            return 3
    else:
        return 0

print(string_compare(first_arg, second_arg))
print(string_compare("What's", "What's"))
print(string_compare("Python", "learn"))
print(string_compare("Pyth", "learn"))
print(string_compare("What's", "updudes"))