import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def square_number(number):
    time.sleep(1)
    return number * number

squared_numbers = []
start_time = time.time()
for number in numbers:
    squared_numbers.append(square_number(number))

end_time = time.time()

print("Squared numbers:", squared_numbers)
print("Time taken:", end_time - start_time, "seconds")
# Time taken: 25.00785255432129 seconds