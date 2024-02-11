import tokenize
from io import BytesIO

def tokenize_string(input_string):
    tokens = []
    input_bytes = input_string.encode('utf-8')
    io_obj = BytesIO(input_bytes)


    for tok in tokenize.tokenize(io_obj.readline):
        tokens.append(tok) 

    return tokens




# Example Usage : 

code_string = "print(4+2)"
tokens = tokenize_string(code_string)


for token in tokens:
    print(token)