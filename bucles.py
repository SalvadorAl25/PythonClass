for item1 in range(3):
    for item2 in range(5):
        print("item1 = "+str(item1)+", item2 = "+str(item2))

print("\n------------------------------------")

item1 = 0
while item1<3:
    for item2 in range(5):
        print("item1 = " + str(item1)+", item2 = "+str(item2))
    item1 = item1 +1

print("\n-------------------------------")

item1 = 0
while item1 < 3:
    item2 = 0
    while item2<5:
        print("item1 = " + str(item1)+",item2 = "+str(item2))
        item2 = item2 + 1
    item1 = item1 + 1
    