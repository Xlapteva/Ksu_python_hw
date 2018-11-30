user_age = int(input("How old are you?"))

def occupation(user_age):
    
    if user_age < 6:
        return "Kindergarten"

    elif 6 <= user_age <= 17: 
        return "School"

    elif 18 <=user_age <= 22: 
        return "Uni" 

    elif 23<= user_age <= 90:
        return "Work" 

    else:
        return "Probably dead"

print(occupation(user_age))

