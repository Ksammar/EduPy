# Реализовать функцию int_func(), принимающую слова из маленьких
# латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
def int_func(arg):
    return str(arg).title()


print(int_func('text'))
list_str = input('insert any words ').split()
for words in list_str:
    print(int_func(words))
