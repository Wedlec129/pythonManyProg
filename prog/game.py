#SOKOLOV BE KKCO-04-21
#
from itertools import count
from os import system
from sys import exit



def misionOne():
	print("норд:    эй ты не спишь, ты нарушитель границ, да?")
	print("норд:    надо же тебе было попасть в имперскую засаду. они и нас поймали и ворюгу этого..")
	print("вор:  проклятые братья бури.в скайриме было тихо пока вас сюда не занесло. имеперии не до чего дела не было.")
	print("имперский солдат:    А НУ, ВСЕ ЗАТКНУЛИСЬ")
	print("!повозка остановидась!")
	print("!вор попытался сбежать. но его попвтка была тщетной) *выстрел в колено*!")
	print("имперский солдат:    тебя в списке на казнь нет, кто ты ?")
	nameHero=input("> ")

	print("имперский солдат:    тебя в списке нет. но мы всё равно отрубим теье голову")

	print("!вашу казнь прервал дракон!")

	print("вы пойдёте за имперцец или за братьем бури")

	while True:
		choice=input("> ").lower()

		if choice =="имперец":
			print("вы пошли за имперцем он дал вам оружие")
			misionTwo("имперец")
			exit(0)
		if choice=="бури":
			print("вы пощли за братьем бури он дал вам оружие и ведро")
			misionTwo("бури")
			exit(0)
		else:
			print("введите коректные данные")




def printMap(map,x,y):
	
	system("clear")
	

	for row in map:
		print("")
		for elem in row:
			print(elem, end=' ')
			


def dead(why):
	print("GAME OVER")
	print(f"ТЫ не драконорождённый, убит: {why}")
	exit(0)


def win():
		print("YOU ARE WIN")
		print("вы герой skyrim, о вашем подвиге ходят легенды.....")
		exit(0)

def misionTwo(who):
	x=1
	y=1
	maps = [
		["#", "#", "#", "#","#", "#", "#", "#"], 
		["#", " ", "#", " "," ", " ", " ", "#"], 
		["#", " ", "#", " ","#", " ", " ", "#"],
		["#", " ", " ", " ","#", " ", " ", "#"],
		["#", "D", "#", " "," ", "D", "W", "#"],
		["#", "#", "#", "#","#", "#", "#", "#"]]


	while True:
		 
		maps[x][y]="H"
		printMap(maps,x,y)
		
		print("\n\nH - 		ИГОРК")
		print("D - 		ОПАСНОСТЬ")
		print("W - 		ПОБЕДА")
	
		print("\n вы находитесь в комнате, куда пойдёте? (право,лево,низ,верх)")
		choice=input(">")

        
		if choice=="право":
			maps[x][y]=" "

			if maps[x][y+1]=="W":
				win()
			if maps[x][y+1]=="D":
				dead("орк отправил вас в небо")	
			if maps[x][y+1]!="#":
				y+=1	


		if choice=="лево":
			maps[x][y]=" "

			if maps[x][y-1]=="W":
				win()
			if maps[x][y-1]=="D":
				dead("орк отправил вас в небо")	
			if maps[x][y-1]!="#":
				y-=1	


		if choice=="низ":
			maps[x][y]=" "

			if maps[x+1][y]=="С":
				coin+=1
			if maps[x+1][y]=="W":
				win()
			if maps[x+1][y]=="D":
				dead("орк отправил вас в небо")	
			if maps[x+1][y]!="#":
				x+=1	


		if choice=="верх":
			maps[x][y]=" "
			if maps[x-1][y]=="W":
				win()
			if maps[x-1][y]=="D":
				dead("орк отправил вас в небо")	
			if maps[x-1][y]!="#":
				x-=1
    
		

def start():
	
	misionOne()
	#misionTwo("бури")








start()
