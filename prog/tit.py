from tkinter import * #библиоека
 
window = Tk()
window.title("Графическая программа на Python")
window.geometry("900x600+200+300") #w h x y
 
 
#TEXT
txt = Label(window, text="Привет",font=("Arial Bold", 11),foreground="white",  # Устанавливает белый текст
    background="black",width=20,
    height=10 ) # Устанавливает черный фон
txt.grid(column=0, row=0) #отображаем в окне
txt.place(x=100, y=100)



button =Button(
    text="Нажми на меня!",
    
)
button.grid(column=0, row=0) #отображаем в окне
button.place(x=250, y=100)




window.mainloop()







