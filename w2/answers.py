
def ask_user():
    
    diction = {"Как дела": "Хорошо", 
    "Что делаешь?":"Программирую", 
    "И как тебе":"Нормально"}

    looking_for = "Хорошо"
    user_says = ""
    while user_says != looking_for:
        try:
            user_says = input("Как дела?")
            print(diction.get(user_says, "Dunno"))
        except KeyboardInterrupt: 
            print("Пока")
            break    

ask_user()