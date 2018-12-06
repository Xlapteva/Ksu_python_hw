# Прочитайте содержимое файла в переменную, подсчитайте длинну получившейся строки

# with open('referat.txt', 'r', encoding = 'utf-8') as referat:
#     data = referat.read()
#     print(len(data)) 


# Подсчитайте количество слов в тексте

# with open('referat.txt', 'r', encoding = 'utf-8') as referat:
#     data = referat.read()
#     data = data.split()
#     num_words = len(data)

# print(num_words)

# Замените точки в тексте на восклицательные знаки
with open('referat.txt', 'r', encoding = 'utf-8') as referat:
    data = referat.read()
    data = data.replace('.','!')
    print(data)

    with open('referat2.txt', 'w', encoding = 'utf-8') as ref2:
        ref2.write(data)
        