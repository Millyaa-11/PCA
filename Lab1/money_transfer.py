money = int(input())
bank = str(input())
bankB = "kk"
total = 0

if bank == bankB:
    if money > 10000:
        fee = money * 0.01
        total = money + fee
    else:
        total = money
else:
    fee = (money * 0.01) + 50
    total = money + fee
print (total)
