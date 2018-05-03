import numpy as np
import matplotlib.pyplot as plt

x1 = 1.5
x2 = 2.5
x3 = 2.8
x4 = 5.0

def func(x,lamda):
	return np.exp(-x/lamda)/(lamda*(np.exp(-1.0/lamda)-np.exp(-20.0/lamda)))

lista = [x1,x2,x3,x4]
lamda=np.linspace(0.1,30,100)
probabilidad=np.ones(100)
total=0.0
n = len(probabilidad)
for i in range(n):
	for j in range(0,4):
		probabilidad[i] = probabilidad[i]*func(lista[j],lamda[i])
	total+=probabilidad[i]
	
probabilidad=probabilidad/total
plt.plot(lamda,probabilidad, c = "m")
plt.xlabel('Lambda')
plt.ylabel('probabilidad(Lambda|x)')
plt.title("Grafica")
plt.savefig('grafica_1.png')
