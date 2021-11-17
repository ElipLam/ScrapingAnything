import re
import time
import csv
string = '188.000₫'
string2 = 'ARS$ 224,99'
string3 = 'Free'
string4 = '-75,9%'
pattern = r'\d+\.\d+|\d+,\d+'

result = re.search(pattern, string)
result2 = re.search(pattern, string2)
result3 = re.split(result2.group(), string2)
# print(result.group())
# print(result2.group())
# print(result3)
# print(len(result3[0]))

def clear_percentage(string):
    pattern = r'%'
    clear_percent = re.sub(pattern,'', string)
    result= re.sub(',','.',clear_percent)
    return float(result)



def clean_text(string):
    pattern_new_line = r'\n'
    clean_n_result = re.sub(pattern_new_line, '', string)
    pattern_multi_spaces = r'\s\s+'
    result1 = re.sub(pattern_multi_spaces, ' ', clean_n_result)
    pattern_head_tail_spaces= r'^\s+|\s+$'
    result = re.sub(pattern_head_tail_spaces, '', result1)

    return result


def get_price_and_currency(raw):
    pattern = r'\d+\.\d+|\d+,\d+'
    if re.search(pattern, raw):
        price = re.search(pattern, raw).group()
        list_unit_currency = re.split(price, raw)
        unit = ''
        for unit_currency in list_unit_currency:
            if len(unit_currency) == 0:
                continue
            unit = clean_text(unit_currency)
        print(f'price: {price}, unit: {unit}')
        return (price, unit)
    else:
        print(raw)
        return raw

start_time = time.time()
kq = get_price_and_currency(string)
kq2 = get_price_and_currency(string2)
kq3 = get_price_and_currency(string3)
print(type(kq))
print(type(kq2))
print(type(kq3))
end_time = time.time()
elapsed = end_time - start_time
print(clear_percentage(string4))
print( clean_text('1    Header'))

lines =[] 
csv_file_path="test_csv_save"
file_name = f"{csv_file_path}.csv"
with open("test_csv_save.csv") as f:
    csvflie =f.readlines()
    print(csvflie)