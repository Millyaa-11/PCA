print("1 : from dec \n2 : to dec")
f = int(input())

def from_dec(b, n):
    ans = []
    hexDict = {"10" : "A", "11" : "B", "12" : "C", "13" : "D", "14" : "E", "15" : "F", "16" : "G", "17" : "H", "18" : "I", "19" : "J", "20" : "K", "21" : "L", "22" : "M", "23" : "N", "24" : "O", "25" : "P", "26" : "Q", "27" : "R", "28" : "S", "29" : "T", "30" : "U", "31" : "V", "32" : "W", "33" : "X", "34" : "Y", "35" : "Z"}

    while n >= 1:
        r = n % b
        #r is the remainder of number dividing with b
        n = n // b
        #number = number rounded divided base
        if b >= 16 and r > 9:
            x = str(r)
            #convert remainder to string
            hexAl = (hexDict[x])
            #get the hexdict value of remainder
            ans.append(hexAl)

        else:
            ans.append(r)
    ans.reverse()
    #reverse the ans list order
    return ans

def to_dec(b,s):
    hexDict = {"A" : "10", "B" : "11", "C" : "12", "D" : "13", "E" : "14", "F" : "15", "G" : "16", "H" : "17", "I" : "18", "J" : "19", "K" : "20", "L" : "21", "M" : "22", "N" : "23", "O" : "24", "P" : "25", "Q" : "26", "R" : "27", "S" : "28", "T" : "29", "U" : "30", "V" : "31", "W" : "32", "X" : "33", "Y" : "34", "Z" : "35"}
      
    lst = [*str(s)]
    #split string s to list
    lst.reverse()
    d = 0
    for i in range (len(lst)):
        if lst[i] in hexDict.keys():
        #if list[i] is in the dictionary key
            x = int(hexDict[lst[i]])
            #convert dictionary to int
            d += x * (b ** i)
        else:
            d += int(lst[i]) * (b ** i)
            #d = d + reverse int s list * (b power i)
    return d

if f == 1:
    print ("Enter base : ")
    b = int(input())
    print("Enter decimal : ")
    n = int(input())

    print (from_dec(b, n))

elif f == 2:
    print ("Enter base : ")
    b = int(input())
    print ("Enter remainder : ")
    s = str(input())

    print (to_dec(b,s))

else:
    print ("error")