#Takes in 2 scoring matrixes and figures out how many points to give the player. Qual determines whether the letters are green or yellow, and Quant helps track how many points to give out per letter. 

def pointdist(list1,list2):
    qual = [0,0,0,0,0]
    code = 0
    while code == 0:
        quant = [0,0,0,0,0]
        k = sum(list2[0]) + sum(list2[1]) + sum(list2[2]) + sum(list2[3]) + sum(list2[4])
        for i in range(len(qual)):
            if list1[i][i] == list2[i][i] and list1[i][i] == 1:
                    qual[i] = 2
                    quant[i] = 1
        for i in range(len(qual)):
            for j in range(len(qual)):
                if list1[i][j] == 1 and sum(quant) < int(k**(1/2)):
                    if qual[j] == 2:
                        qual[j] = 2
                    elif list1[i][j] == 1 and qual[j] != 2:
                        qual[j]=1
                        quant[j] = 1
                    else:
                        continue

            code = 1
    return qual







