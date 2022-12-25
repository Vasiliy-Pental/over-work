import time
day = int(input('Enter the number of working days in the current month : '))
moneyInMonth = int(input('Monthly salary? : '))
ata = day * 8
money = moneyInMonth / ata
print(f'One hour of work is worth {round(money,1)}')
print("The script will close automatically after 5 seconds")
for x in reversed(range(1,6)):
    time.sleep(1)
    print(x)
print('See you soon')