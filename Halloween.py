import random

class House:

    #def __init__(self): ?

    #def getRating(): ?
        

    def goodPath(self, m, s, num):
        #randPath & greedyPath
        p = []
        q = []
        t = 1
        while (s/25 > t/num):
            p = []
            q = []
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            z = 0
            p.append([x, y])
            q = set(map(tuple, p))
            t = m[x][y]
            #print([x, y])
            
            while (len(p) < num):
                a = random.randint(-1, 1)
                b = random.randint(-1, 1)
                while ((not a + b == 1) and (not a + b == -1)) or (not 0 <= x+a <= 4) or (not 0 <= y+b <= 4):
                    a = random.randint(-1, 1)
                    b = random.randint(-1, 1)
                else:
                    x = x + a
                    y = y + b
                    p.append([x, y])
                    q = set(map(tuple, p))
                    if len(q) == len(p):
                        t = t + m[x][y]
                        #print([x, y])
                        a = 0
                        b = 0
                        z = 0
                    else:
                        x = x - a
                        y = y - b
                        z = z + 1
                        del p[len(p)-1]
                        q = set(map(tuple, p))
                        if z > 10:
                            #print("Refreshing...")
                            break
            else:
                print("Finished!")
                print("Calculating the average...")
        else:
            print("\nWe found a good path for you!")
            print(p)
            print("The average rate of your path is '"+ str(t/num) + "', while")
            print("the average rate of all the houses is '" + str(s/25) + "' .")
        

def main():

    h = House()

    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(random.randint(1, 10))
            
            #h = House() ?
            #l.append(h.getRating()) ?
            
    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])
    s = 0
    for i in range(5):
        s = s + m[0][i] + m[1][i] + m[2][i] + m[3][i] + m[4][i]

    num = int(input("How many houses?\n"))
    while (not 0<num<=25):
        num = int(input("How many houses?\n"))
        
    h.goodPath(m, s, num)
    
if __name__ == "__main__":
    main()
        
