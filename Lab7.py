#Raul Rodriguez
#80549657
#Last Modified - 11/26/2018
#Diego Aguirre - Professor
#Manoj Saha - Assistant

def edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)

    # if one of the strings is empty
    if n * m == 0:
        return n + m

    # array to store the convertion
    d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = d[i - 1][j] + 1
            down = d[i][j - 1] + 1
            left_down = d[i - 1][j - 1]
            if word1[i - 1] != word2[j - 1]:
                left_down += 1
            d[i][j] = min(left, down, left_down)
    return d[n][m]

def main():
    word1 = "money"
    word2 = "miners"
    print(word1+ "," + word2)
    print(edit_distance(word1, word2))
    print()
    
    word1 = "intention"
    word2 = "execution"
    print(word1 +","+  word2)
    print(edit_distance(word1, word2))
    print()
    
    word1 = "game"
    word2 = "race"
    print(word1 +","+  word2)
    print(edit_distance(word1, word2))

main()