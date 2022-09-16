class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return Integer(int(value))
        except ValueError or TypeError:
            return "wrong type"


first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))