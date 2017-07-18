import re
import operator

text = "Show me all Samsung LCD TVs. Show me all Samsung LCD Televisions. Show me all LCD TVs by Samsung. \
Show me all LCD TVs from Samsung. Show me all LCD Televisions by Samsung. Show me all LCD Televisions from Sony."

expression = "([A-Z][a-z]*)?\sLCD\s(TVs?|Televisions?)(\s(from|by)\s([A-Z][a-z]*))?"

matches = re.findall(expression, text)
brands = {}

for match in matches:
    if match[0] != '':
        brands[match[0]] = brands.get(match[0], 0) + 1
    elif match[-1] != '':
        brands[match[-1]] = brands.get(match[-1], 0) + 1

sorted_brands = sorted(brands.iteritems(), key=operator.itemgetter(1), reverse=True)

for brand in sorted_brands:
    print brand[0], brand[1]
