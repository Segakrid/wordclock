from datetime import datetime, time

words = """
H E T k I S a v i j f
t i e n b t z v o o r
o v e r m e k w a r t
h a l f s p w o v e r
v o o r t h g e e n s
t w e e p v c d r i e
v i e r v i j f z e s
z e v e n o n e g e n
a c h t t i e n e l f
t w a a l f b f u u r
"""

new_words = words

while True:
    now = datetime.now()
    now_time = now.time()
    previous_words = new_words

    if 0 <= int(str(now_time)[3:5]) <= 4:
        new_words = new_words.replace("u u r", "U U R", 1)

    if 5 <= int(str(now_time)[3:5]) <= 9:
        new_words = words.replace("v i j f", "V I J F", 1)
        new_words = new_words.replace("w o v e r", "w O V E R", 1)

    elif 10 <= int(str(now_time)[3:5]) <= 14:
        new_words = words.replace("t i e n", "T I E N", 1)
        new_words = new_words.replace("w o v e r", "w O V E R", 1)

    elif 15 <= int(str(now_time)[3:5]) <= 19:
        new_words = words.replace("k w a r t", "K W A R T", 1)
        new_words = new_words.replace("w o v e r", "w O V E R", 1)

    elif 20 <= int(str(now_time)[3:5]) <= 24:
        new_words = words.replace("t i e n", "T I E N", 1)
        new_words = new_words.replace("v o o r", "V O O R", 1)
        new_words = new_words.replace("h a l f", "H A L F", 1)

    elif 25 <= int(str(now_time)[3:5]) <= 29:
        new_words = words.replace("v i j f", "V I J F", 1)
        new_words = new_words.replace("v o o r", "V O O R", 1)
        new_words = new_words.replace("h a l f", "H A L F", 1)

    elif 30 <= int(str(now_time)[3:5]) <= 34:
        new_words = words.replace("h a l f", "H A L F", 1)

    elif 35 <= int(str(now_time)[3:5]) <= 39:
        new_words = words.replace("v i j f", "V I J F", 1)
        new_words = new_words.replace("o v e r", "O V E R", 1)
        new_words = new_words.replace("h a l f", "H A L F", 1)

    elif 40 <= int(str(now_time)[3:5]) <= 44:
        new_words = words.replace("t i e n", "T I E N", 1)
        new_words = new_words.replace("o v e r", "O V E R", 1)
        new_words = new_words.replace("h a l f", "H A L F", 1)

    elif 45 <= int(str(now_time)[3:5]) <= 49:
        new_words = words.replace("k w a r t", "K W A R T", 1)
        new_words = new_words.replace("v o o r t", "V O O R t", 1)

    elif 50 <= int(str(now_time)[3:5]) <= 54:
        new_words = words.replace("t i e n", "T I E N", 1)
        new_words = new_words.replace("v o o r t", "V O O R t", 1)

    elif 55 <= int(str(now_time)[3:5]) <= 59:
        new_words = words.replace("v i j f", "V I J F", 1)
        new_words = new_words.replace("v o o r t", "V O O R t", 1)

    if int(str(now_time)[0:2]) == 0 or int(str(now_time)[0:2]) == 12:
        new_words = new_words.replace("t w a a l f", "T W A A L F", 1)
    elif int(str(now_time)[0:2]) == 1 or int(str(now_time)[0:2]) == 13:
        new_words = new_words.replace("e e n", "E E N", 1)
    elif int(str(now_time)[0:2]) == 2 or int(str(now_time)[0:2]) == 14:
        new_words = new_words.replace("t w e e", "T W E E", 1)
    elif int(str(now_time)[0:2]) == 3 or int(str(now_time)[0:2]) == 15:
        new_words = new_words.replace("d r i e", "D R I E", 1)
    elif int(str(now_time)[0:2]) == 4 or int(str(now_time)[0:2]) == 16:
        new_words = new_words.replace("v i e r", "V I E R", 1)
    elif int(str(now_time)[0:2]) == 5 or int(str(now_time)[0:2]) == 17:
        new_words = new_words.replace("v i j f z", "V I J F z", 1)
    elif int(str(now_time)[0:2]) == 6 or int(str(now_time)[0:2]) == 18:
        new_words = new_words.replace("z e s", "Z E S", 1)
    elif int(str(now_time)[0:2]) == 7 or int(str(now_time)[0:2]) == 19:
        new_words = new_words.replace("z e v e n", "Z E V E N", 1)
    elif int(str(now_time)[0:2]) == 8 or int(str(now_time)[0:2]) == 20:
        new_words = new_words.replace("a c h t", "A C H T", 1)
    elif int(str(now_time)[0:2]) == 9 or int(str(now_time)[0:2]) == 21:
        new_words = new_words.replace("n e g e n", "N E G E N", 1)
    elif int(str(now_time)[0:2]) == 10 or int(str(now_time)[0:2]) == 22:
        new_words = new_words.replace("t i e n e", "T I E N e", 1)
    elif int(str(now_time)[0:2]) == 11 or int(str(now_time)[0:2]) == 23:
        new_words = new_words.replace("e l f", "E L F", 1)

    if previous_words != new_words:
        print
        print now_time
        print new_words