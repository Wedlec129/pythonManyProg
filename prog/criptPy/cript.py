import pyAesCrypt
import os
import sys


# функция шифрования файла
def encryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директорий шифрования файла
def walking_by_dirsEcryption(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirsEcryption(path, password)


# функция дешифровки файла
def decryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директорий дешифровки файла
def walking_by_dirsDecryption(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirsDecryption(path, password)


# ф-я определяет папка или файл ("Folder" / "Fille" )
def FolderOrFille(path):
    # если конец "/" -> папка
    if (path.rfind("/") == len(path) - 1):
        return "Folder"
        #print("это папка")

    else:
        # если не нашли точку -> папка
        if (path[path.rfind("/") + 1:len(path)]).find(".") == -1:
            return "Folder"
            #print("это папка")
        else:
            return "Fille"
            #print("это файл")












watWont=input("Ведите план действий : шифрование (1) или ДЕшифрование (2) : ")

if watWont=="1":


    file = str(input("Введите путь до папки/файла : "))

    password = input("Введите пароль для шифрования : ")

    if(FolderOrFille(file)=="Folder") :
        walking_by_dirsEcryption(file, password)
    else:
        encryption(file, password)

if watWont=="2":
    file = str(input("Введите путь до папки/файла : "))

    password = input("Введите пароль для ДЕшифрования : ")

    if (FolderOrFille(file) == "Folder"):
        walking_by_dirsDecryption(file, password)
    else:
        decryption(file, password)

