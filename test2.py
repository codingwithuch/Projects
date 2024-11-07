


def convtoonesandzeros(wordgen,wordguess,letter):
    var1 = wordgen
    var2 = wordguess
    compare = []
    for i in range(len(var1)):
        u = []
        for j in range(len(var2)):
            u.append([var2[i],var1[j]])
        compare.append(u)
    for i in range(len(var2)):
        for j in range(len(var2)):
            if compare[i][j][0] == compare[i][j][1] and compare[i][j] == [letter,letter]:
                compare[i][j] = 1
            else:
                compare[i][j] = 0
    return(compare)
