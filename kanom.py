""" Kanom """
def main():
    """ Kanom """
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    money2 = float((money - water)%3)
    if money2 == 0:
        var1 = money - (snack1*10)
    elif money2 == 1:
        var2 = money - (snack1*15)
    elif money2 == 2:   
        var3 = money - (snack1*20)