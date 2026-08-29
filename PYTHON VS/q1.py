# q1.py

def analyze_list():
    n = int(input().strip())
    numbers = list(map(int, input().split()))
    
    if not numbers:
        return

    largest = numbers[0]
    smallest = numbers[0]
    total_sum = 0
    even_count = 0
    odd_count = 0
    reversed_list = []

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total_sum += num
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Sum: {total_sum}")
    print(f"Even count: {even_count}")
    print(f"Odd count: {odd_count}")
    print("Reversed:", *reversed_list)

if __name__ == "__main__":
    analyze_list()
