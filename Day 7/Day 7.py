import re
# input_file = 'Day 7\\Input.csv'
input_file = 'Day 7\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

for line in lines:
    m = re.split(r"\[(\w+)\]", line)
    print(m)


#index even = outside of brackets, index odd = inside brackets (so it seems)