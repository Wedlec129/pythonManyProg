


def writeFille(sms):
  sms=sms.replace(" ", "")
  with open("/Users/wedlec/Desktop/lol.txt", "w") as file:
    file.write(sms)


def readFille(name):
     name=name.replace(" ", "")
     line=""
     Clearline=""
     with open("/Users/wedlec/Desktop/lol.txt", "r") as file:
        line = file.read()
    
    
     #print(line)
     index=line.find(name)+len(name)
     #print(index)
     
     stop=0
     i=1
     while stop==0:
      #print(line[index+i])
      Clearline=Clearline+line[index+i]
      if line[index+i+1]==';':
       stop=1
       
      else :
       i=i+1
     
     return Clearline







     ##WRITE FILLE
age=19;
mony=120;
    
string=str("age="+str(age)+"; "+"mony="+str(mony)+";") #делаем строку которую запишем
writeFille(string)


      ##READ FILLE
    
age2 = int(readFille("age")); # читаем строку и ищем значение age  и переводим в число
    
print(age2)
