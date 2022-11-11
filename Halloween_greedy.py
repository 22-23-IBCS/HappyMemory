import random
import copy
import sys
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

class House:
        
    def bestPath(self, s, m, num, houses, coords):
        
        bestCoords = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        bestSelection = []
        for i in range(25):
            bestCoords[i].append(coords[i])
            
        for i in range(num-1):
            for j in range(25):
                compareHouses = []
                compareCoords = []
                for k in range(len(bestCoords[24])):
                    x = bestCoords[j][k][0]
                    y = bestCoords[j][k][1]
                    if x < 4:
                        compareHouses.append(m[x+1][y])
                        compareCoords.append([x+1, y])
                    if x > 0:
                        compareHouses.append(m[x-1][y])
                        compareCoords.append([x-1, y])
                    if y < 4:
                        compareHouses.append(m[x][y+1])
                        compareCoords.append([x, y+1])
                    if y > 0:
                        compareHouses.append(m[x][y-1])
                        compareCoords.append([x, y-1])
                        
                for l in range(len(compareHouses)):
                    for e in range(l):
                        if compareHouses[l]>compareHouses[e]:
                            compareHouses.insert(e, compareHouses[l])
                            compareCoords.insert(e, compareCoords[l])
                            del compareHouses[l+1]
                            del compareCoords[l+1]
                l = 0            
                while l == 0:
                    for e in range(len(compareCoords)):
                        check = []
                        check.append(compareCoords[e])
                        del compareCoords[e]
                        if check[0] in compareCoords:
                            l = 0
                            del compareHouses[e]
                            break
                        else:
                            l = 1
                            compareCoords.insert(e, check[0])
                            
                for p in range(len(compareCoords)):
                    for q in range(len(bestCoords[j])):
                        if compareCoords[p]!= bestCoords[j][q]:
                            z = 1
                            continue
                        else:
                            z = 2
                            break
                    if z == 1:
                        if (i < num-2):
                            bestCoords[j].append(compareCoords[p])
                            new = houses[j] + compareHouses[p]
                            houses.insert(j, new)
                            del houses[j+1]
                            break
                        elif (i == num-2):
                            wait = copy.copy(bestCoords[j])
                            wait.append(compareCoords[p])
                            bestSelection.append(wait)
                            new = houses[0] + compareHouses[p]
                            houses.append(new)
                if i == num-2:
                    del houses[0]

            if (i < num-2):
                for j in range(25):
                    for k in range(j):
                        if houses[j]>=houses[k]:
                            houses.insert(k, houses[j])
                            bestCoords.insert(k, bestCoords[j])
                            del houses[j+1]
                            del bestCoords[j+1]
            elif (i == num-2):
                for j in range(len(bestSelection)):
                    for k in range(j):
                        if houses[j]>=houses[k]:
                            houses.insert(k, houses[j])
                            bestSelection.insert(k, bestSelection[j])
                            del houses[j+1]
                            del bestSelection[j+1]

        for i in range(len(bestSelection)):
            sample = copy.copy(bestSelection[i])
            inherit = []
            route = []
            for j in range(len(bestSelection[i])):
                select = [[], [], [], []]
                for k in range(len(sample)):
                    x = sample[k][0]
                    y = sample[k][1]
                    z = 0
                    e = 0
                    f = 0
                    if [x, y+1] in sample:
                        z = z+1
                    if [x, y-1] in sample:
                        z = z+1
                    if [x+1, y] in sample:
                        z = z+1
                    if [x-1, y] in sample:
                        z = z+1
                        
                    if z == 0:
                        select[0].append([x, y])
                    if z == 1:
                        select[1].append([x, y])
                    if z == 2:
                        select[2].append([x, y])
                    if z == 3:
                        select[3].append([x, y])
                if (len(select[1]) >= 3) or (len(select[0]) >= 1) :
                    #print("No way")
                    break
                elif (len(select[1]) == 0) and (j == 0):
                        e = 1
                        #print("Yes way")
                        break
                else:
                    #print("Try")
                    if j == 0:
                        p = select[1][0][0]
                        q = select[1][0][1]
                        inherit.append([p, q+1])
                        inherit.append([p, q-1])
                        inherit.append([p+1, q])
                        inherit.append([p-1, q])
                        route.append(select[1][0])
                        sample.remove(select[1][0])
                    elif j >= 1:
                        for u in range(3):
                            for v in range(4):
                                for w in range(len(select[u+1])):
                                    if inherit[v] == select[u+1][w]:
                                        break
                                else:
                                    continue
                                break
                            else:
                                continue
                            break
                        p = select[u+1][w][0]
                        q = select[u+1][w][1]
                        inherit = []
                        inherit.append([p, q+1])
                        inherit.append([p, q-1])
                        inherit.append([p+1, q])
                        inherit.append([p-1, q])
                        route.append(select[u+1][w])
                        sample.remove(select[u+1][w])
                        if (len(sample) == 1):
                            route.append(sample[0])
                            #print("Yes way")
                            f = 1
                            break
                        
            if (e == 1) or (f == 1):
                break
            else:
                continue

        if (len(bestSelection) == 0):
            i = 0
            f = 1
            wait = []
            wait.append(coords[i])
            bestSelection.append(wait)
            route = copy.copy(bestSelection[i])

        elif (i == len(bestSelection)-1) and (e != 1) and (f != 1):
            i = 0
            if (len(bestSelection[i]) == 2):
                f = 1
                route = copy.copy(bestSelection[i])

        print("We foud a very good path for you!")
        print(" ")
        for a in range(5):
            for b in range(5):
                if [b, a] in bestSelection[i]:
                    if m[b][a] == 10:
                        color.write("T", "KEYWORD")
                        color.write(" ")
                        if b == 4:
                            color.write("\n")
                    else:
                        color.write(str(m[b][a]), "KEYWORD")
                        color.write(" ")
                        if b == 4:
                            color.write("\n")
                else:
                    if m[b][a] == 10:
                        color.write("T")
                        color.write(" ")
                        if b == 4:
                            color.write("\n")
                    else:
                        color.write(str(m[b][a]))
                        color.write(" ")
                        if b == 4:
                            color.write("\n")
        print(" ")
        print("※ T = 10")
        print("※ The orange area is your path!")
        if f == 1:
            print(route)
        print(" ")
        print("The total candy you'll get is '" + str(houses[i]) + "' .")
        print("The average number of candy you get is '" + str(houses[i]/num) + "', while")
        print("the average number of all the houses is '" + str(s/25) + "' .")


def main():

    h = House()

    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(random.randint(1, 10))
            
            #h = House() ?
            #l.append(h.getRating()) ?

    for a in range(5):
        for b in range(5):
            if m[b][a] == 10:
                color.write("T", "DEFINITION")
                color.write(" ")
                if b == 4:
                    color.write("\n")
            else:
                color.write(str(m[b][a]), "DEFINITION")
                color.write(" ")
                if b == 4:
                    color.write("\n")
    print("※ T = 10")
            
    s = 0
    for i in range(5):
        s = s + m[0][i] + m[1][i] + m[2][i] + m[3][i] + m[4][i]

    num = int(input("How many houses?\n"))
    while (not 0<num<=25):
        num = int(input("How many houses?\n"))
        
    houses = []
    coords = []
    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])
    for i in range(25):
        for j in range(i):
            if houses[i]>=houses[j]:
                houses.insert(j, houses[i])
                coords.insert(j, coords[i])
                del houses[i+1]
                del coords[i+1]
    
    h.bestPath(s, m, num, houses, coords)
    print(" ")
    color.write("~ Enjoy your Halloween! ~", "hit")
    
    
if __name__ == "__main__":
    main()
