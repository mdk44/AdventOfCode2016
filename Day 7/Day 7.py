import re
# input_file = 'Day 7\\Input.csv'
input_file = 'Day 7\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

for line in lines:
    lst = []
    lst.append(re.split('\] | \[', line))
    print(lst)




import re
a = 'abcd[fgrd]asda'
print(re.split('\[ | \]', a))