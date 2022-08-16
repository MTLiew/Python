import board
import random
import time

startTime = time.time()

states = []
nonAttackers = []
eStrings = []
percentiles = []
selected = []
generations = 1

random.seed()

for i in range(8):
    temp = board.Board(5)
    states.append(temp)
    nonAttackers.append(0)
    eStrings.append("")
    percentiles.append(0)
    selected.append("")

def selection():
    for i in range(8):
        states[i].fitness()
        nonAttackers[i] = (10 - states[i].get_fit())
        eStrings[i] = ""
        
        for j in range(5):
            for k in range(5):
                if states[i].map[j][k] == 1:
                    eStrings[i] += str(k)
                    break
    
    normalizeSum = 0
    for i in range(8):
        normalizeSum += nonAttackers[i]
    
    for i in range(8):
        nonAttackers[i] = nonAttackers[i]/normalizeSum

        for j in range(8):
            if j <= i:
                percentiles[i] += nonAttackers[j]

    #Nonattacker is currently the percentage
    for i in range(8):
        temp = random.random()

        for j in range(8):
            if temp < percentiles[j]:
                selected[i] = eStrings[j]
                break
            
def crossover():
    for i in range(8):
        temp = random.randint(0, 4)

        #spliceOne is the second half of the first string
        #spliceTwo is the second half of the second string
        if (i + 1) % 2 == 0:
            spliceOne = selected[i - 1][temp:5]
            spliceTwo = selected[i][temp:5]

            selected[i - 1] = selected[i-1][0:temp]
            selected[i - 1] += spliceTwo

            selected[i] = selected[i][0:temp]
            selected[i] += spliceOne

def mutation():
    for i in range(8):
        temp = random.randint(0, 5)
        replace = random.randint(0, 4)

        if temp != 5:
            selected[i] = selected[i][0:temp] + str(replace) + selected[i][temp + 1:5]

flag = 0

while flag == 0:

    for i in range(8):
        states[i].fitness()

        if states[i].get_fit() == 0:
            flag = i
            break
    
    if flag == 0:
        selection()
        crossover()
        mutation()

        for i in range(8):
            for j in range(5):
                for k in range(5):
                    states[i].map[j][k] = 0

                    if selected[i][j:j+1] == str(k):
                        states[i].map[j][k] = 1
    
    generations += 1

totalTime = round((time.time() - startTime) * 1000, 3)
print(totalTime, "ms elapsed.")
print("Number of generations:", generations)
states[flag].show()