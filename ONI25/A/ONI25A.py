inlist = [0, 0]
inlist[0] = int(input())
inlist[1] = int(input())
for i in range(0,inlist[1]):
    inlist.append(input())
lowAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sol = ""
match inlist[0]:
    case 1:
        bigstring = ""
        for i in range(2, inlist[1]+2):
            bigstring = bigstring + inlist[i]
        for letter in lowAlphabet:
            if bigstring.find(letter)==-1:
                sol = sol + letter + " " 
        # Falta tirar o espaço do fim
        sol=sol.rstrip()
        print(sol)
    case 2:
        for i in range(2, inlist[1]+2):
            if inlist[i].find("_") != -1:
                print("snake_case")
            elif inlist[i].find("-") != -1:
                print("kebab-case")
            elif inlist[i][0].islower():
                print("dromedaryCase")
            else:
                print("PascalCase")
    case 3:
        for i in range(2, inlist[1]+2):
            templist=list(inlist[i])
            if inlist[i].find("_") != -1:
                while inlist[i].count("_") > 0:
                    templist[inlist[i].find("_")+1]=templist[inlist[i].find("_")+1].upper()
                    templist.remove("_")
                    inlist[i]="".join(templist)
                print(inlist[i])
            elif inlist[i].find("-") != -1:
                while inlist[i].count("-") > 0:
                    templist[inlist[i].find("-")+1]=templist[inlist[i].find("-")+1].upper()
                    templist.remove("-")
                    inlist[i]="".join(templist)
                print(inlist[i])
            elif inlist[i][0].islower():
                print(inlist[i])
            else:
                templist[0]=templist[0].lower()
                print("".join(templist))