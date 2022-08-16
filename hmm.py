import sys
import math

textFile = sys.argv[1]
arguments = []

with open(textFile) as file:
    lines = file.readlines()

inputLines = len(lines)

for item in lines:
    length = math.ceil(len(item)/2)

    for i in range(5):
        arguments.append(item[4 * i: (4 * i) + 3])
    
    for i in range(10, int(length)):
        arguments.append(item[(2 * i): (2 * i) + 1])

index = 0

for line in range(inputLines):
    iterations = 0
    theEs = []

    a = float(arguments[index])
    b = float(arguments[index + 1])
    c = float(arguments[index + 2])
    d = float(arguments[index + 3])
    f = float(arguments[index + 4])

    index += 5
    
    while arguments[index] == 't' or arguments[index] == 'f':
        theEs.append(arguments[index])

        if index < len(arguments) - 1:
            index += 1
        else:
            break

    iterations = len(theEs)

    innerdex = 0
    
    for time in range(iterations):
        if theEs[innerdex] == 't' and innerdex == 0:
            term1 = d * ((b * a) + (c * (1 - a)))
            term2 = ((1 - b) * a) + ((1 - c) * (1 - a))
            term2 = term2 * f

            observation1 = term1/(term1 + term2)
            observation2 = term2/(term1 + term2)
        
        elif theEs[innerdex] == 't' and innerdex > 0:
            term1 = d * ((b * observation1) + (c * observation2))
            term2 = ((1 - b) * observation1) + ((1 - c) * observation2)
            term2 = term2 * f

            observation1 = term1/(term1 + term2)
            observation2 = term2/(term1 + term2)
        
        elif theEs[innerdex] == 'f' and innerdex == 0:
            term1 = (1 - d) * ((b * a) + (c * (1 - a)))
            term2 = ((1 - b) * a) + ((1 - c) * (1 - a))
            term2 = term2 * (1 - f)

            observation1 = term1/(term1 + term2)
            observation2 = term2/(term1 + term2)
        
        else:
            term1 = (1 - d) * ((b * observation1) + (c * observation2))
            term2 = ((1 - b) * observation1) + ((1 - c) * observation2)
            term2 = term2 * (1 - f)

            observation1 = term1/(term1 + term2)
            observation2 = term2/(term1 + term2)

        innerdex += 1
    
    print(lines[line][0:-1] + "--><%.4f" %observation1 + ",%.4f>" % observation2)
