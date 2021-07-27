def fee(time):
    if time <= 15 :
        money = 0
    elif 15 < time <= 30 :
        money = 3000
    else :
        money = 3000 + 1000 * ((time - 30) // 15) 
    return money

print("40분 주차요금: ", fee(40))
print("50분 주차요금: ", fee(50))