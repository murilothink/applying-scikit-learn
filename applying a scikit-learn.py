#Scikit-learn is a Python library that provides many supervised and unsupervised learning algorithms.
# It is based on some of the technologies you already know, like NumPy, pandas and Matplotlib! ...
# Scikit-learn is a Python library that provides many supervised and unsupervised learning algorithms.
# It is based on some of the technologies you already know, like NumPy, pandas and Matplotlib! In this code
# I will apply it so that we can better understand how it works

from sklearn import tree

pera = 1
verde = 1
morango = 2
vermelho =2
banana = 3
amarela = 3
Laranja = 4
Laranja1 = 4

pomar = [[4, 1],[7,2],[6,3],[7,4]]

resultado = [1,2,3,4]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

input('Escolha uma dessas frutas e memorize: \n BANANA \n PERA \n MORANGO \n LARANJA \n Digite "Ok" para continuar  \n')

peso = input("Quantas letras sua fruta tem?")
surpefice = input("ENTRE COM A COR \n 1 Verde \n 2 Vermelha\n 3 Amarela \n 4 Laranja")

resultadoUsuario = clf.predict([[peso, surpefice]])

if  resultadoUsuario == 1:
    print(" \n Sua fruta é Verde")
elif resultadoUsuario == 2:
    print(" \n Sua fruta é Vermelha")
elif resultadoUsuario == 3:
    print(" \n Sua fruta é Amarela")

else:
    print( " \n É uma laranja")




