import random

trials = 10**6

prob = [0, .9322, .0068, .0610, 0, .4932, .1620, 0, .3448, .4390, 0, .4701, .0909, 0, .1552, .4091, .4357]

def my_mcmc():
    #c, r
    a = 0 #TT
    b = 0 #FT
    c = 0 #TF
    d = 0 #FF
    state = random.randint(1, 4)

    for n in range(trials):
        selected = random.random()
        if state == 1:
            if selected < prob[1]: #1 1
                a += 1
                state = 1
            elif selected >= prob[1] and selected < (prob[1] + prob[2]): #1 2
                c += 1
                state = 2
            else: #1 3
                b += 1
                state = 3
        elif state == 2:
            if selected < prob[5]: #2 1
                a += 1
                state = 1
            elif selected >= prob[5] and selected < (prob[5] + prob[6]): #2 2
                c += 1
                state = 2
            else: #2 4
                d += 1
                state = 4
        elif state == 3:
            if selected < prob[9]: #3 1
                a += 1
                state = 1
            elif selected >= prob[9] and selected < (prob[9] + prob[11]): #3 3
                b += 1
                state = 3
            else: #3 4
                d += 1
                state = 4
        elif state == 4:
            if selected < prob[14]: #4 2
                c += 1
                state = 2
            elif selected >= prob[14] and selected < (prob[14] + prob[15]): #4 3
                b += 1
                state = 3
            else: #4 4
                d += 1
                state = 4
    
    return [(a + c)/trials, (b + d)/trials]

print("Part A. The sampling probabilities")
print(f"P(C| ~s, r) = <{.8780:.4f}, {.1220:.4f}>")
print(f"P(C| ~s, ~r) = <{.3103:.4f}, {.6897:.4f}>")
print(f"P(R| c, ~s, w) = <{.9863:.4f}, {.0137:.4f}>")
print(f"P(R| ~c, ~s, w) = <{.8182:.4f}, {.1818: .4f}>")

print("\nPart B. The transition probability matrix")
print("     S1     S2     S3     S4    ")
print(f"S1 {prob[1]:.4f} {prob[2]:.4f} {prob[3]:.4f} {prob[4]:.4f}")
print(f"S2 {prob[5]:.4f} {prob[6]:.4f} {prob[7]:.4f} {prob[8]:.4f}")
print(f"S3 {prob[9]:.4f} {prob[10]:.4f} {prob[11]:.4f} {prob[12]:.4f}")
print(f"S4 {prob[13]:.4f} {prob[14]:.4f} {prob[15]:.4f} {prob[16]:.4f}")

results = my_mcmc()

print("\nPart C. The probability for the query")
print(f"P(C| ~s, w) = <{results[0]}, {results[1]}>")


