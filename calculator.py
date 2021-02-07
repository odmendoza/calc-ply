from math_expresions_lexer import lexer

print("\t**********************************************")
print("\t***      Math calculator | Welcome !       ***")
print("\t**********************************************")

while True:
    data = input(">_ ")
    # Give the lexer the input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        # print(tok.type, tok.value, tok.lineno, tok.lexpos)
