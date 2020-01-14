input_file = 'Day 9\\Input.csv'
# input_file = 'Day 9\\Test1.csv'
# input_file = 'Day 9\\Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

line = 'ADVENT'
line = 'A(1x5)BC'
line = '(3x3)XYZ'
line = 'A(2x2)BCD(2x2)EFG'
line = '(6x1)(1x3)A'
line = 'X(8x2)(3x3)ABCY'