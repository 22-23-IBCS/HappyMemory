import random

class House:

    #def __init__(self): ?

    #def getRating(): ?
        

    def randPath(self, m, s, num):
        p = []
        q = []
        t = 1
        while (s/25 > t/num) or (len(q) < len(p)):
            p = []
            q = []
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            p.append([x, y])
            q = set(map(tuple, p))
            t = m[x][y]
            while (len(p) < num) and (len(q) == len(p)):
                a = random.randint(-1, 1)
                b = random.randint(-1, 1)
                while ((not a + b == 1) and (not a + b == -1)) or (not 0 <= x+a <= 4) or (not 0 <= y+b <= 4):
                    a = random.randint(-1, 1)
                    b = random.randint(-1, 1)
                    p.append([x+a, y+b])
                    q = set(map(tuple, p))
                    if len(q) < len(p):
                        #r = len(p)-1
                        for i in range(len(p)-1):
                            if p[i-1] == p[len(p)-1]:
                                del p[i-1]
                                break
                            else:
                                print("WAIT")   
                    else:
                        print("WAIT")
                else:
                    x = x + a
                    y = y + b
                    print(x)
                    print(y)
                    p.append([x, y])
                    q = set(map(tuple, p))
                    t = t + m[x][y] 
            else:
                print("WAIT...")
        else:
            print("We found a good path for you!")
            print(p)
            print("The average rate of your path is '"+ str(t/num) + "', while the average rate of all the houses is '" + str(s/25) + "' .")
        

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
    
    """for i in range(25):
        if num == i:
            break
        else:
            continue
    if not num == 1:
        num = int(input("How many houses?\n"))"""

    h.randPath(m, s, num)
    
    
if __name__ == "__main__":
    main()
        
