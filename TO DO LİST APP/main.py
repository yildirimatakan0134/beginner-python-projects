ToDoList = []

def gorevekle(ToDoList):
    gorev = input("yapılacak gorevı gırınız: ")
    ToDoList.append(gorev)
    print("gorev basarıyla eklendı!")

def gorevlerı_goster(toDoList):
    sirasayisi = 0
    for i in toDoList:
        sirasayisi +=1
        print(sirasayisi,"-") + i

def gorevsıl(toDoList):
   gorev = input("silinecek olan gorevı secınız: ")
   if gorev in toDoList:
       toDoList.remove(gorev)
       print("gorev basarıyla sılındı")
   else:
       print("gorev bulunamadı...")




while True:
    print("\n to Do List uygulamasına hosgeldınız")
    print("\n yapmak ıstedıgınız gorevı secınız: "
          "\n 1 - gorev ekle"
          "\n 2 - gorevlerı goster"
          "\n 3 - gorev sil"
          "\n 4 - uygulamadan cıkıs yap")

    secım = int(input("lutfen secımınızı gırınız : 1/2/3/4"))

    if secım ==1 :
        gorevekle(ToDoList)

    elif secım ==2 :
        gorevlerı_goster(ToDoList)

    elif secım ==3 :
        gorevsıl(ToDoList)

    elif secım ==4 :
        print("uygulamadan cıkılıyor...")
        break


    else:
        print("gecersiz secim yaptınız...")

