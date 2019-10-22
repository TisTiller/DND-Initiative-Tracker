

print("Format: NAME (No Spaces), Initiative\ne.g. Tyler 11")
while True:
    mainList, final = [], []

    # Get items for list of initiatives
    while True:
        m = input("> ")
        if m:  
            mainList.append([i for i in m.split(" ")])
        else:
            break
    print(f"Participants: {len(mainList)}")
    
    # Sorting the participants
    for x in range(len(mainList)):
        biggest = ["Example", "-10"]
        num = 0
        for i in mainList:
            if int(i[1]) > int(biggest[1]):
                biggest = i

    # Get the location of the largest (current) initative
        for i in mainList:
            if i == biggest:
                break
            else:
                num += 1
        final.append(biggest)
        mainList.pop(num)

    # Ordered Output
    print(f"Final order:")
    for i in final:
        diffLen = 20 - len(i[0])
        print(i[0]," "*diffLen, i[1], sep = '')
    print("--- END --- \n\n")
        
