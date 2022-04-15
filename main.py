def who_is_winner(pieces_position_list):
    plansza = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    for element in pieces_position_list:
        nie_wiem = element.split('_')
        kolumna_litera = nie_wiem[0]
        gracz = nie_wiem[1]
        a_value = ord('A')
        kolumna = ord(kolumna_litera)-a_value
        if gracz == "Red":
            kolor_gracza = 1
        else:
            kolor_gracza = 2
        wrzuc(kolumna, kolor_gracza, plansza)
        wynik = wygrany(plansza)
        if wynik != "Draw":
            return wynik
    return wygrany(plansza)


def wrzuc(kolumna,gracz,plansza):
    puste_miejsce = len(plansza[kolumna])-1
    for index, p in enumerate(plansza[kolumna]):
        if p != 0:
            puste_miejsce = index - 1
            break

    plansza[kolumna][puste_miejsce] = gracz

def print_plansza(plansza):
    for i in plansza:
        for j in i:
            print(j," ",end='')
        print()

def wygrany(plansza):
    w1 = "Draw"
    for index_x, x in enumerate(plansza):
        for index_y, y in enumerate(x):
            #print(index_x,index_y)
            if index_x-3 >= 0 and plansza[index_x][index_y] == 1 and\
                    plansza[index_x-1][index_y] == 1 and plansza[index_x-2][index_y] == 1 and plansza[index_x-3][index_y] == 1:
                w1 = "Red"

            elif index_y-3 >= 0 and plansza[index_x][index_y] == 1 and\
                    plansza[index_x][index_y-1] == 1 and plansza[index_x][index_y-2] == 1 and plansza[index_x][index_y-3] == 1:
                w1 = "Red"
            elif index_y - 3 >= 0 and index_x - 3 >= 0 and plansza[index_x][index_y] == 1 and \
                    plansza[index_x-1][index_y - 1] == 1 and plansza[index_x-2][index_y - 2] == 1 and plansza[index_x-3][index_y - 3] == 1:
                w1 = "Red"
            elif index_y - 3 >= 0 and index_x + 3 <= len(plansza)-1 and plansza[index_x][index_y] == 1 and \
                    plansza[index_x + 1][index_y - 1] == 1 and plansza[index_x + 2][index_y - 2] == 1 and\
                    plansza[index_x + 3][
                        index_y - 3] == 1:
                w1 = "Red"
            if index_x - 3 >= 0 and plansza[index_x][index_y] == 2 and \
                    plansza[index_x - 1][index_y] == 2 and plansza[index_x - 2][index_y] == 2 and plansza[index_x - 3][index_y] == 2:
                w1 = "Yellow"

            elif index_y - 3 >= 0 and plansza[index_x][index_y] == 2 and \
                    plansza[index_x][index_y - 1] == 2 and plansza[index_x][index_y - 2] == 2 and plansza[index_x][index_y - 3] == 2:
                w1 = "Yellow"
            elif index_y - 3 >= 0 and index_x - 3 >= 0 and plansza[index_x][index_y] == 2 and \
                    plansza[index_x - 1][index_y - 1] == 2 and plansza[index_x - 2][index_y - 2] == 2 and \
                    plansza[index_x - 3][
                        index_y - 3] == 2:
                w1 = "Yellow"
            elif index_y - 3 >= 0 and index_x + 3 <= len(plansza) - 1 and plansza[index_x][index_y] == 2 and \
                    plansza[index_x + 1][index_y - 1] == 2 and plansza[index_x + 2][index_y - 2] == 2 and \
                    plansza[index_x + 3][
                        index_y - 3] == 2:
                w1 = "Yellow"
    return print(w1)


who_is_winner([
"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
"B_Yellow", "B_Red"
])