import imp
from subprocess import call
from tools.col import *
from tools.numbers.comp import *
from tools.numbers.simp import *

def main():
    called_simp = False
    while True:
        print("1 - add two numbers")
        print("2 - substract two numbers")
        print("3 - get sum of digits in a number")
        print("4 - check if palindrome")
        print("5 - zip two collections")
        print("e - quit")

        inp = input("Input: ")
        if inp == "e":
            break
        elif inp == "1":
            num1 = input("First number: ")
            num2 = input("Second number: ")
            try:
                print(add_numbers(int(num1),int(num2)))
                called_simp = True
            except:
                print("Error! Make sure to use numbers and not text.")
        elif inp == "2":
            num1 = input("First number: ")
            num2 = input("Second number: ")
            try:
                print(substract_numbers(int(num1),int(num2)))
                called_simp = True
            except:
                print("Error! Make sure to use numbers and not text.")
        elif inp == "3":
            if called_simp:
                num = input("Your number: ")
                try:
                    print(sum_digits(int(num)))
                except:
                    print("Error! Make sure to use numbers and not text.")
            else:
                print("Call a simple function (option 1 or 2) first!")
        elif inp == "4":
            if called_simp:
                num = input("Your number: ")
                try:
                    pal = ispal(int(num))
                    if pal:
                        print("Is a palindrome!")
                    else:
                        print("Not a palindrome!")
                except:
                    print("Error! Make sure to use numbers and not text.")
            else:
                print("Call a simple function (option 1 or 2) first!")
        elif inp == "5":
            lst1 = []
            lst2 = []

            try:
                n1 = int(input("Enter number of elements in first list: "))
                for i in range(0, n1):
                    ele = int(input())
                    lst1.append(ele)

                n2 = int(input("Enter number of elements in second list: "))
                for i in range(0, n2):
                    ele = int(input())
                    lst2.append(ele)
            except:
                print("Error! Make sure to use numbers and not text.")

            try:
                print(list(zip_two(lst1,lst2)))
            except:
                print("Unexpected error!")
        


if __name__ == "__main__":
    main()