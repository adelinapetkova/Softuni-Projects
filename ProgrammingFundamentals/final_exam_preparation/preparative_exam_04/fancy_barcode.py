import re

n = int(input())
regex_for_barcode = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for _ in range(n):
    is_valid = False
    barcode = input()
    valid_barcode = re.findall(regex_for_barcode, barcode)
    if len(valid_barcode) > 0:
        is_valid = True
    if not is_valid:
        print("Invalid barcode")
    else:
        digits_in_barcode = ''.join(re.findall(r'\d', barcode))
        if digits_in_barcode=='':
            print('Product group: 00')
        else:
            print(f'Product group: {digits_in_barcode}')
