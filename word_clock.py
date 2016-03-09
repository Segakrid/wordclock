__author__ = 'Dirk'

from time import strftime

time_in_words = []

if int(strftime("%H")) == 0 or int(strftime("%H")) == 12:
    if int(strftime("%M")) < 20:
        time_in_words.append("twaalf")
    else:
        time_in_words.append("een")

elif int(strftime("%H")) == 1 or int(strftime("%H")) == 13:
    if int(strftime("%M")) < 20:
        time_in_words.append("een")
    else:
        time_in_words.append("twee")

elif int(strftime("%H")) == 2 or int(strftime("%H")) == 14:
    if int(strftime("%M")) < 20:
        time_in_words.append("twee")
    else:
        time_in_words.append("drie")

elif int(strftime("%H")) == 3 or int(strftime("%H")) == 15:
    if int(strftime("%M")) < 20:
        time_in_words.append("drie")
    else:
        time_in_words.append("vier")

elif int(strftime("%H")) == 4 or int(strftime("%H")) == 16:
    if int(strftime("%M")) < 20:
        time_in_words.append("vier")
    else:
        time_in_words.append("vijf")

elif int(strftime("%H")) == 5 or int(strftime("%H")) == 17:
    if int(strftime("%M")) < 20:
        time_in_words.append("vijf")
    else:
        time_in_words.append("zes")

elif int(strftime("%H")) == 6 or int(strftime("%H")) == 18:
    if int(strftime("%M")) < 20:
        time_in_words.append("zes")
    else:
        time_in_words.append("zeven")

elif int(strftime("%H")) == 7 or int(strftime("%H")) == 19:
    if int(strftime("%M")) < 20:
        time_in_words.append("zeven")
    else:
        time_in_words.append("acht")

elif int(strftime("%H")) == 8 or int(strftime("%H")) == 20:
    if int(strftime("%M")) < 20:
        time_in_words.append("acht")
    else:
        time_in_words.append("negen")

elif int(strftime("%H")) == 9 or int(strftime("%H")) == 21:
    if int(strftime("%M")) < 20:
        time_in_words.append("negen")
    else:
        time_in_words.append("tien")

elif int(strftime("%H")) == 10 or int(strftime("%H")) == 22:
    if int(strftime("%M")) < 20:
        time_in_words.append("tien")
    else:
        time_in_words.append("elf")

elif int(strftime("%H")) == 11 or int(strftime("%H")) == 23:
    if int(strftime("%M")) < 20:
        time_in_words.append("elf")
    else:
        time_in_words.append("twaalf")

time_in_words = [x.upper() for x in time_in_words]

if 0 <= int(strftime("%M")) <= 4:
    time_in_words.insert(0, "het is")
    time_in_words.append("uur")

elif 5 <= int(strftime("%M")) <= 9:
    time_in_words.insert(0, "over")
    time_in_words.insert(0, "vijf")

elif 10 <= int(strftime("%M")) <= 14:
    time_in_words.insert(0, "over")
    time_in_words.insert(0, "tien")

elif 15 <= int(strftime("%M")) <= 19:
    time_in_words.insert(0, "over")
    time_in_words.insert(0, "kwart")

elif 20 <= int(strftime("%M")) <= 24:
    time_in_words.insert(0, "half")
    time_in_words.insert(0, "voor")
    time_in_words.insert(0, "tien")

elif 25 <= int(strftime("%M")) <= 29:
    time_in_words.insert(0, "half")
    time_in_words.insert(0, "voor")
    time_in_words.insert(0, "vijf")

elif 30 <= int(strftime("%M")) <= 34:
    time_in_words.insert(0, "half")
    time_in_words.insert(0, "het is")

elif 35 <= int(strftime("%M")) <= 39:
    time_in_words.insert(0, "half")
    time_in_words.insert(0, "over")
    time_in_words.insert(0, "vijf")

elif 40 <= int(strftime("%M")) <= 44:
    time_in_words.insert(0, "half")
    time_in_words.insert(0, "over")
    time_in_words.insert(0, "tien")

elif 45 <= int(strftime("%M")) <= 49:
    time_in_words.insert(0, "voor")
    time_in_words.insert(0, "kwart")

elif 50 <= int(strftime("%M")) <= 54:
    time_in_words.insert(0, "voor")
    time_in_words.insert(0, "tien")

elif 55 <= int(strftime("%M")) <= 59:
    time_in_words.insert(0, "voor")
    time_in_words.insert(0, "vijf")

print
print strftime("%H.%M")
print
for word in time_in_words:
    print word,
