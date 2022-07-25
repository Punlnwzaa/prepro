""" Drop """
def main():
    """ Drop """
    grade1 = float(input())
    grade2 = (2*2)-grade1
    if grade1 < 1.00:
        print("I'm so sad.")
    elif grade1 < 2.00 and grade1 >= 1.00:
        print("%.2f" %grade2)
    elif grade1 >= 2.00 and grade1 <= 4.00:
        print("I'm so happy.")
main()
