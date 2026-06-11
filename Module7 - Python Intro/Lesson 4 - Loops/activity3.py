# Python program to calculate the sum of the first ten natural numbers using a while loop

total_sum = 0
num = 1
last_number = 45

while num <= last_number:
    total_sum += num
    num += 1

print(f"The sum of the first {last_number} natural numbers is {total_sum}")