r = int(input("enter a number to convert into roman numerals: "))

class RomanConverter:
    def __init__(self):
        self.roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def to_roman(self, num):
        if not (1 <= num <= 3999):
            raise ValueError("Integer must be between 1 and 3999.")

        roman_numeral = ""
        temp_num = num

        for value, symbol in self.roman_map:
            while temp_num >= value:
                roman_numeral += symbol
                temp_num -= value
        return roman_numeral

converter = RomanConverter()
print(f"{r} is {converter.to_roman(r)}")
