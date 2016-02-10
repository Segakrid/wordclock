from datetime import datetime, time

now = datetime.now()
now_time = now.time()
time_text = "Het is"



if 5 <= int(str(now_time)[3:5]) <= 9 or 35 <= int(str(now.time)[3:5]) <= 39:
	time_text += " vijf"
	time_text += " over"
	
if 10 <= int(str(now_time)[3:5]) <= 14 or 40 <= int(str(now.time)[3:5]) <= 44:
	time_text += " tien"
	time_text += " over"
	
if 15 <= int(str(now_time)[3:5]) <= 19:
	time_text += " kwart"
	time_text += " over"
	


if 20 <= int(str(now_time)[3:5]) <= 24:
	time_text += " tien"
	time_text += " voor"
	time_text += " half"
	
#if str(now_time)[0:2] == "23" or str(now_time)[0:2] == "11" and not "half" in time_text:
#	time_text += " elf"
if str(now_time)[0:2] == "23" and "half" in time_text or str(now_time)[0:2] == "11" and "half" in time_text:
	time_text += " twaalf"

if 0 <= int(str(now_time)[3:5]) <= 4:
	time_text += " uur"

print str(now_time)[0:2]
print str(now_time)[3:5]
print time_text
print now_time
