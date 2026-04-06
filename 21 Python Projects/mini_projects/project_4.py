# Time Module in python
import time

ctm = input("Please enter your timeout in this format - hh-mm-ss: ")
total_seconds = 0
for idx, item in enumerate(ctm.split("-")):
    if idx==0:
        total_seconds+=(int(item) * 60 *60)
    elif idx ==1:
        total_seconds+=(int(item) * 60)
    else:
        total_seconds += int(item)
current_time = time.time()
timeout_time = current_time + total_seconds
while True:
    time.sleep(1)
    if time.time() >= timeout_time:
        print("Alarm!")
        break
    else:
        print("Not Yet")
