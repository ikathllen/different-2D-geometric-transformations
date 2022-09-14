# Realizar as diferentes transformações geométricas em 2D.
# Elas são: Translação, Escala, Reflexão, Rotação e Cisalhamento.

#biblioteca necessárias 
import numpy as np 
import matplotlib.pyplot as plt
import math

#pontos para a formação da figura, sendo que ela será um retangulo de 1 à 3 no eixo X e de 1 à 2 no eixo Y
x1 = np.array([1,3,3,1,1])
y1 = np.array([1,1,2,2,1])

#valores para os pontos do gráfico, será usado para todos de uma forma ampla para poder verificar as transformações
Xvalues = [-3,-2,-1,0,1,2,3,4,5,6]
Yvalues = [0,1,2,3,4] 

plt.subplot(2, 3, 1)
#plotagem normal do gráfico
plt.plot(x1,y1, marker="o", color="red")
plt.title("gráfico")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()
plt.subplot(2, 3, 2)
plt.plot(x1,y1, marker="o", color="blue")
#plotagem do gráfico de transalação, o qual faz a soma com +2 no eixo X e +2 no eixo Y
plt.plot(x1+2,y1+2, marker="o", color="red")
plt.title("Translação")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()
plt.subplot(2, 3, 3)
plt.plot(x1,y1, marker="o", color="blue")
#plotagem do gráfico escalar, o qual faz a multiplica de *2 no eixo X e *2 no eixo Y
plt.plot(x1*2,y1*2, marker="o", color="red")
plt.title("Escalar")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()
plt.subplot(2, 3, 4)
plt.plot(x1,y1, marker="o", color="blue")
#plotagem do gráfico de reflexão, o qual possui reflexão no eixo X
plt.plot(-x1,y1, marker="o", color="red")
plt.title("Reflexão")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()
plt.subplot(2, 3, 5)
plt.plot(x1,y1, marker="o", color="blue")
#plotagem do gráfico de rotação, utilizando 0 = 15 rad e a formula:
# para o eixo X (x.cos(0) - y.sen(0))
# para o eixo Y (y.cos(0) + x.sen(0))
plt.plot(((x1*np.cos(math.radians(15))) - (y1*np.sin(math.radians(15)))), ((y1*np.cos(math.radians(15))) + (x1*np.sin(math.radians(15)))), marker="o", color="red")
plt.title("Rotação")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()
plt.subplot(2, 3, 6)
plt.plot(x1,y1, marker="o", color="blue")
#plotagem do gráfico de cisalhamento, considerando a constante K(x) = 1, K(y) = 0 e a formula:
# para o eixo X (x + (Kx*y))
# para o eixo Y (y + (Ky*x))
plt.plot((x1+(1*y1)),(y1+(0*x1)), marker="o", color="red")
plt.title("Cisalhamento")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()

plt.show()

