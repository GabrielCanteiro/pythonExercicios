#Explorar as caracteristcas de uma string ou Number
inf = input('digite algo:')
print('o tipo primitivo desse valor é ',type(inf))
print('só tem espacos?',inf.isspace())
print('é um numero?',inf.isalnum())
print('é uma letra?',inf.isalpha())
print('é um Alfa numerico ?',inf.isalnum())
print('está maiusculo?',inf.isupper())