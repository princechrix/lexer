
__author__ = 'ISHIMWE Prince Christian <princechrix.dev@gmail.com>'



import basic 

while True:
    text = input("kinyaScrpit :: > ")
    result, error = basic.run('<stdin>', text)


    if error:
        print(error.as_string())
    else:
        print(result)