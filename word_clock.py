__author__ = 'Dirk'

from time import strftime

line_one = ["h e t", "k", "i s", "a", "v i j f"]
line_two = ["t i e n", "b t z", "v o o r"]
line_three = ["o v e r", "m e", "k w a r t"]
line_four = ["h a l f", "s p w", "o v e r"]
line_five = ["v o o r", "t h g", "e e n", "s"]
line_six = ["t w e e", "p v c", "d r i e"]
line_seven = ["v i e r", "v i j f", "z e s"]
line_eight = ["z e v e n", "o", "n e g e n"]
line_nine = ["a c h t", "t i e n", "e l f"]
line_ten = ["t w a a l f", "b f", "u u r"]

all_lines = [line_one, line_two, line_three, line_four, line_five, line_six, line_seven, line_eight, line_nine, line_ten]

if int(strftime("%H")) == 8 or int(strftime("%H")) == 20 and int(strftime("%M")) < 20:
    line_nine[1]
print
print strftime("%H")
print strftime("%M")
print
for line in all_lines:
    for i in line:
        print i,
    print
# for i in line_two:
#     print i,
# print
# for i in line_three:
#     print i,
# print
# for i in line_four:
#     print i,
# print
# for i in line_five:
#     print i,
# print
# for i in line_six:
#     print i,
# print
# for i in line_seven:
#     print i,
# print
# for i in line_eight:
#     print i,
# print
# for i in line_nine:
#     print i,
# print
# for i in line_ten:
#     print i,