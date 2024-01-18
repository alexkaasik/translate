from random import*
rus_list = []
ang_list = []
est_list = []

langs = ["est","rus","eng"]

def pick(rus_list, ang_list, est_list):
    
    T = (input("translate, add, game, fix or quit\nInput:")).lower()
    if T == "quit":
        print("bye")
        exit()
    if T == "add":
        new_word(rus_list, ang_list, est_list)

    z = 0
    for x in langs:
        for y in langs:
            if x != y:
                print(f"{z} {x} -> {y}")
                z+=1

    mode = int(input("in what mode "))
    
    while True:
        if ( mode == 0 ):
            mas1 = est_list
            mas2 = rus_list
            f1 = "est.txt"
            f2 = "rus.txt"
        elif ( mode == 1 ):
            mas1 = est_list
            mas2 = ang_list
            f1 = "est.txt"
            f2 = "ang.txt"
        elif ( mode == 2 ):
            mas1 = rus_list
            mas2 = est_list
            f1 = "rus.txt"
            f2 = "est.txt"
        elif ( mode == 3 ):
            mas1 = rus_list
            mas2 = ang_list
            f1 = "rus.txt"
            f2 = "ang.txt"
        elif ( mode == 4 ):
            mas1 = ang_list
            mas2 = est_list
            f1 = "ang.txt"
            f2 ="est.txt"
        elif ( mode == 5 ):
            mas1 = ang_list
            mas2 = rus_list
            f1 = "ang.txt"
            f2 = "rus.txt"
        else:
            continue
        break   

    
    if T == "fix":
        change(mas1, mas2,f1,f2)
    elif T == "game":
        game(mas1, mas2)
    elif T == "translate":
        tolkimine(mas1, mas2)
    elif T == "quit":
        print("bye")
        exit()
      
def loe_failist(f):
    fail = open(f,'r',encoding="utf-8-sig")
    mas = [] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def tolkimine(mas1,mas2):
    sona = input("insert a word to translate\ninput:")
    if sona in mas1:
        tolk = mas2[mas1.index(sona)]
    elif sona in mas2:
        tolk = mas1[mas2.index(sona)]
    else:
        tolk = "null"

    print(f"{sona}--{tolk}")
    return pick(mas1,mas2)

def new_word(mas1,mas2,mas3):
    while True:
        sona_Rus = input("input a русское слово\nInput:")
        sona_Eng = input("input a English word\nInput:")
        sona_Est = input("input a Eesti keel sona\nInput:")
        yn = str(input("is this the right translations?"))
        if yn[0].lower() == "n":
            break

    mas1.append(sona_Rus)
    mas2.append(sona_Eng)
    mas3.append(sona_Est)

    fail = open("rus.txt",'a',encoding="utf-8-sig")
    fail.write(sona_Rus+"\n")
    fail.close()
    fail = open("ang.txt",'a',encoding="utf-8-sig")
    fail.write(sona_Eng+"\n")
    fail.close()
    fail = open("est.txt",'a',encoding="utf-8-sig")
    fail.write(sona_Est+"\n")
    fail.close()
    
    return pick(rus_list,ang_list,est_list)

def change(mas1, mas2,f1,f2):
    sona = input("word to remove\nInput:")
    if sona in mas1:
        tolk = mas2[mas1.index(sona)]
        f2.remove(tolk)
        f1.remove(sona)
    elif sona in mas2:
        tolk = mas1[mas2.index(sona)]
        f1.remove(tolk)
        f2.remove(sona)
    else:
        print("again\n")
        return change(f1,f2)
    
    new_word(rus_list,ang_list,'rus.txt','ang.txt')

def game(mas2, mas1):
    G=int(input("how many questions\nInput:"))
    print(len(mas1))
    while G > len(mas1):
        G=int(input("how many questions agian\nInput:"))
    
    l=len(mas2)
    l2=G
    for i in range(0,G):
        a=randint(0,l-1)
        a1=mas2[a]
        q=input(f"{i+1}){a1}\nyour russian answer\nInput:")
        if mas1[a] == q:
            l2-=1
            print(f"good\n{l2} left\n")
        else:
            l2-=1
            print(f"bad\n{l2} left\n")

    if l2 == G:
        mark = "5"
    elif round(G*0.8) <= l2 <= G:
        mark = "4"
    elif round(G*0.6) <= l2 <= round(G*0.8):
        mark = "3"
    elif round(G*0.4) <= l2 <= round(G*0.6):
        mark = "2"
    elif round(G*0.2) <= l2 <= round(G*0.4):
        mark = "1"
    else:
        mark = "fail"
    print(f"{l2}/{G}\nYou got {l2/G*100}%--grade:{mark}")

    return pick(rus_list,ang_list,est_list)

rus_list = loe_failist('rus.txt')
ang_list = loe_failist('ang.txt')
est_list = loe_failist('est.txt')

rus_list,ang_list = pick(rus_list,ang_list,est_list)
pick(rus_list,ang_list,est_list)