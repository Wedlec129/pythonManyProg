###SETINGS


putDoExitFille="/Users/wedlec/Desktop/mein.py/myLib/getMousePosition/exitGetMousePos.txt"




#####
from pynput.mouse import Button, Controller
mouse = Controller()
#print("позиция курсора "+ str(mouse.position) ) #дать позицию курсора
strPos=str((mouse.position))

strPos=strPos.replace("(", "")
strPos=strPos.replace(")", "")
strPos=strPos.replace(" ", "")


index=strPos.find(",")

#print(strPos)

#разделяем до запятой
strPosClearX=strPos[:index]
strPosClearY=strPos[index+1:]


index=strPos.find(".")
strPosClearX=strPosClearX[:index+2] #округляем до точки


index=strPos.find(".")
strPosClearY=strPosClearY[:index+2] #округляем до точки




x=float(strPosClearX)
y=float(strPosClearY)
strPosClearX=0
strPosClearY=0

x=int(x)
y=int(y)



with open(putDoExitFille, "w") as file:
    file.write(str(x))
    file.write(" ")
    file.write(str(y))
