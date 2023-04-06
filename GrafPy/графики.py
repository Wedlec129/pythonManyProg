
#библиотеки
import numpy as np
import matplotlib.pyplot as plt

################################################

formula="y=x**2-2x+2"

diapazon=[-100,100] # диапазон X

###############################################

##убираем лишнее в формуле и меняем X на массив

#ставим знак умножения 7x->7*x
for i in  range(0,len(formula)-1):
    if formula[i].isdigit() and formula[i+1]=='x': #если число и сдед x
        formula = formula[:i+1], '*', formula[i+1:]  #вставляем по индексу знак умножения
        formula = "".join(formula) #cоединяем строку, так как мы её меняли

#убираем лишнее
formula=formula.replace("y", " ")
formula=formula.replace("=", " ")
formula=formula.replace(" ", "")
formula=formula.replace("x", "x[len(x)-1]")





x = []
y = []




#заполняем x и y
for i in range(diapazon[0],diapazon[1]):
    x.append(i)

    y.append(eval(formula)) # используем строку как код

#выводим x и y
if 1==2:
 #выводим x и y
 for i in range(0,len(x)):
     print("x = "+ str(x[i]) )
     print("y = "+str(y[i]) )
     print("               ")



plt.plot(x,y,color='red')





plt.show()