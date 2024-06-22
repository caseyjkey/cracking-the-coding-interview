# Given a number, print the English version e.g. One Thousand, Two Hundred Thirty Four
ones = {
        0: '', 1: "One", 2: "Two", 3: "Three",
        4: "Four", 5: "Five", 6: "Six", 7: "Seven",
        8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven",
        12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
        16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
    }
tens = {
        2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
        6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninenty"
    }
illions = {
        1: "Thousand,", 2: "Million,", 3: "Billion,", 4: "Trillion,",
        5: "Quadrillion,", 6: "Quintillion,", 7: "Sextillion,", 8: "Septillion,",
        9: "Octillion,", 10: "Nonillion,", 11: "Decillion,"
    }

def say_number(i: int) -> str:
    if i < 0:
        return _join('Negative', _say_number_pos(-i))
    if i == 0:
        return 'Zero'
    return _say_number_pos(i)

def _say_number_pos(i: int) -> str:
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'Hundred')
    for illions_number, illions_name in illions.items():
        if i < 1000**(illions_number + 1):
            break
    return _divide(i, 1000**illions_number, illions_name)

def _divide(dividend: int, divisor: int, magnitude: str) -> str:
    return _join(
            _say_number_pos(dividend // divisor),
            magnitude,
            _say_number_pos(dividend % divisor)
        )

def _join(*args):
    return ' '.join(filter(bool, args))

number = int(input("Enter a number:"))

print(say_number(number))
    
