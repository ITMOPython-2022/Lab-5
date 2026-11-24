import re


line = "Давайте обрабатывать строкз 24 часа в сутки"

line0 = '''Renault Logan, 2015 г.в., в605ен178
        Ford Fusion, 2017 г.в., а 301 рр 198
        Volkswagen Polo, 2013 г.в., у617оо-147
        Lada Granta, 2011 г.в., с313ур 98
        Иж-21251, 1991 г.в., д 2139 ЛГ'''

line2 = 'IP address to find: 127.0.0.1 or 192.168.0.1 or 10.77.70.11 but not 111.612.257.002'
line3 = 'Римские числа: XVII, XLXI, XII, CXVI'
line4 = 'RGB hsfdvs colors: #1AFFa1, #171c3a, #72CAD5, #ABC, #bac0'

# result = re.findall(r'\w\s?\d{3,4} ?\w{2}(?:[ -]?\d{2,3})?', line0)
# result = re.findall(r'\b(?=\w)M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})(?!\w|-)\b', line3)
# result = re.findall(r'(?:\b|^)(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.1?\d\d?|2[0-4]\d|25[0-5]){3}(?=$|\W)', line2)
result = re.findall(r'\w{6}(?!:)', line4)
print(result)

# ()[]{}/\|.?*+^$
# \d -> [0-9] - \D -> [^0-9]
# \w -> [а-яА-ЯёЁ_] - \W -> [^а-яА-ЯёЁ_]
# \s -> [ \n\t\v\f] - \S
# ? -> {0,1}
# + -> {1,}
# * -> {0,}
# \b -> граница слова
# \Q и \E
# (?=шаблон) и (?!шаблон) - просмотр вперед
# (?<=шаблон) и (?<!шаблон) - просмотр назад