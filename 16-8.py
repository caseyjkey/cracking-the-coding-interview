# Given a number, print the English version e.g. One Thousand, Two Hundred Thirty Four

numToWord = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
number = int(input("Enter a number:"))
print(numToWord[number])

