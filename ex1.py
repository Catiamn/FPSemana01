name_1 = str(input())
atk_1 = int(input())
def_1 = int(input())

name_2 = str(input())
atk_2 = int(input())
def_2 = int(input())

name_3 = str(input())
atk_3 = int(input())
def_3 = int(input())

char_1 =[name_1, (atk_1, def_1)]
char_2 =[name_2, (atk_2, def_2)]
char_3 =[name_3, (atk_3, def_3)]
char_list =[char_1+ char_2 +char_3]

print(char_list)

if (atk_1 < atk_3 and atk_2 < atk_3):
    print("Ataque "+name_3+" "+str(atk_3))
elif (atk_2 < atk_1 and atk_3 < atk_1):
    print("Ataque "+name_1+" "+str(atk_1))
elif (atk_1 < atk_2 and atk_3 < atk_2):
    print("Ataque "+name_2+" "+str(atk_2))

if (def_1 < def_3 and def_2 < def_3):
    print("Defesa "+name_3+" "+str(def_3))
elif (def_2 < def_1 and def_3 < def_1):
    print("Defesa "+name_1+" "+str(def_1))
elif (def_1 < def_2 and def_3 < def_2):
    print("Defesa "+name_2+" "+str(def_2))