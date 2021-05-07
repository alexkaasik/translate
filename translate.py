from random import*
rus_list = []
ang_list = []

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
    return pick(rus_list,ang_list)

def new_word(mas1,mas2,f1,f2):
    sona_Rus = input("input a Russain word\nInput:")
    sona_Eng = input("input a English word\nInput:")
    mas1.append(sona_Rus)
    mas2.append(sona_Eng)
    fail = open(f1,'a',encoding="utf-8-sig")
    fail.write(sona_Rus+"\n")
    fail.close()
    fail = open(f2,'a',encoding="utf-8-sig")
    fail.write(sona_Eng+"\n")
    fail.close()
    print(f"rus{rus_list}\nang{ang_list}")
    return pick(rus_list,ang_list)

def pick(rus_list,ang_list):
    T = input("translate, add, game or fix\nInput:")
    if T == "add":
        new_word(rus_list,ang_list,'rus.txt','ang.txt')
    elif T == "fix":
        change(rus_list,ang_list)
    elif T == "game":
        game()
    elif T == "translate":
        tolkimine(rus_list,ang_list)
    else:
        print("sorry")
        return pick(rus_list,ang_list)

def change(mas1,mas2):
    sona = input("word to remove\nInput:")
    if sona in mas1:
        tolk = mas2[mas1.index(sona)]
        ang_list.remove(tolk)
        rus_list.remove(sona)
    elif sona in mas2:
        tolk = mas1[mas2.index(sona)]
        rus_list.remove(tolk)
        ang_list.remove(sona)
    else:
        print("again\n")
        return change(rus_list,ang_list)
    
    new_word(rus_list,ang_list,'rus.txt','ang.txt')

def game():
    G=int(input("how many questions\nInput:"))
    print(len(rus_list))
    while G > len(rus_list):
        G=int(input("how many questions agian\nInput:"))
    AR=input("rus to eng(re)  or eng to rus(er)")
    if AR=="er":
        l=len(ang_list)
        l2=G
        for i in range(0,G):
            a=randint(0,l-1)
            a1=ang_list[a]
            q=input(f"{i+1}){a1}\nyour russian answer\nInput:")
            if rus_list[a] == q:
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

    else:
        l=len(rus_list)
        l2=G
        for i in range(0,G):
            a=randint(0,l-1)
            a1=ang_list[a]
            q=input(f"{i+1}){a1}\nyour russian answer\nInput:")
            if rus_list[a] == q:
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

    return pick(rus_list,ang_list)

rus_list = loe_failist('rus.txt')
ang_list = loe_failist('ang.txt')
rus_list,ang_list = pick(rus_list,ang_list)
pick(rus_list,ang_list)