import shelve
import time


with shelve.open('Fruittest') as fruit:
    fruit['orange'] = "Oragnger fruit"
    fruit['grape'] = "For wine"
    fruit['banana'] = "yummy"

print(time.localtime())
print("perf_counter():", time.get_clock_info('perf_counter'))