#Scikit-learn is a Python library that provides many supervised and unsupervised learning algorithms.
# It is based on some of the technologies you already know, like NumPy, pandas and Matplotlib! ...
# Scikit-learn is a Python library that provides many supervised and unsupervised learning algorithms.
# It is based on some of the technologies you already know, like NumPy, pandas and Matplotlib! In this code
# I will apply it so that we can better understand how it works

from sklearn import tree

pera = 1
morango = 2
banana = 3
Laranja = 4
maca = 2
melancia = 2
abacaxi = 1

pomar = [[4,4,1],[7,4,2],[6,1,3],[7,3,4],[4,4,2], [8,4,1], [7,1,1]]

resultado = [1,2,3,4,5,6,7]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

input('Escolha uma dessas frutas e memorize: BANANA  PERA  MORANGO  LARANJA  MAÇA  MELANCIA  ABACAXI \n Digite "Ok" para continuar  ')

peso = input(" \n Quantas letras sua fruta tem?")

primeira_letra = input(" \n ESCOLHA UM GRUPO QUE CONSIDERE A PRIMEIRA LETRA DA SUA FRUTA \n ABCD Digite 1 \n EFGH Digite 2 \n IJKL Digite 3 \n MNOP Digite 4 \n QRST Digite 5 \n UVWXYZ Digite 6 ")

surpefice = input(" \n ENTRE COM A COR \n 1 Verde \n 2 Vermelha\n 3 Amarela \n 4 Laranja")

resultadoUsuario = clf.predict([[peso,primeira_letra, surpefice]])

if  resultadoUsuario == 1:
    print(" \n Sua fruta é Pera")
elif resultadoUsuario == 2:
    print(" \n Sua fruta é Morango ")
elif resultadoUsuario == 3:
    print(" \n Sua fruta é Banana")

elif resultadoUsuario == 4:
    print("Sua Fruta é uma Laranja")

elif resultadoUsuario == 5:
    print( " \n É uma maça")

elif resultadoUsuario == 6:
    print(" \n É uma Melancia")

else:
    print( " \n É uma Abacaxi")





