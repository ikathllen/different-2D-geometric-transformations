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
plt.title("grafico")
plt.xticks(Xvalues)
plt.yticks(Yvalues)
plt.grid()

plt.show()

