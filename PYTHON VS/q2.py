def process_list(numbers):
    new_list = numbers.copy()
    positive_only = []
    for num in new_list:
        if num >= 0:
            positive_only.append(num)
    positive_only.append(0)
    positive_only.sort()
    return positive_only

if __name__ == "__main__":
    original = list(map(int, input().split()))
    result = process_list(original)
    print("Original:", original)
    print("Result:", result)