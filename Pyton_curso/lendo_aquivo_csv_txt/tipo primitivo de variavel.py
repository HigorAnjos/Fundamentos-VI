variavel = input("Digite algo: ")
print("so tem espacos? {}".format(variavel.isspace()))
print("e um numero? {}".format(variavel.isnumeric())) #suporta converter a um numero, pois na leitura e um str
print("e alfabetico? {}".format(variavel.isalpha()))
print("e alfanumerico? {}".format(variavel.isalnum()))
print("esta em maiusculas? {}".format(variavel.isupper()))
print("esta em minusculas? {}".format(variavel.islower()))
print("Esta capitalizada? {} ".format(variavel.istitle()))