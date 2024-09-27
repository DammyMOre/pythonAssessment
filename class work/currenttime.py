import time

present_time = time.time()

total_seconds = int(present_time)

seconds =int (total_seconds//60)

total_min = int(seconds/60)

hr = int(total_min % 24+1)

print(hr, total_min,seconds)

