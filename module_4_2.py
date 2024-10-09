def test_function():
    def inner_function():
        print ("Я в области видимости функции test_function")
    inner_function()

test_function()
# inner_function()

# inner_function не может быть вызвана из
# основной порграммы, т.к. она объявлена внутри другой функции,
# следовательно, принадлежит к локальному пространству имён
# функции test_function