prime_numbers = [num for num in range(2, 1001) if all(num % n != 0 for n in range(2, num))]
