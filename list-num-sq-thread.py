import time
from concurrent.futures import ThreadPoolExecutor

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def square_number(number):
    time.sleep(1)
    return number * number

squared_numbers = []
start_time = time.time()

with ThreadPoolExecutor(max_workers=25) as executor:
    results = executor.map(square_number, numbers)

squared_numbers = list(results)

end_time = time.time()

print("Squared numbers:", squared_numbers)
print("Time taken:", end_time - start_time, "seconds")
# Time taken: 1.009631633758545 seconds