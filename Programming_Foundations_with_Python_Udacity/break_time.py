import webbrowser
import time

count = 0
total_breaks = 3

sleep_time = 2 * 60 * 60

print("New day started on " + time.ctime())


while (count < total_breaks):
    time.sleep(sleep_time)
    webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
    count += 1
print("Go home and enjoy your evening")