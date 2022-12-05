from string import ascii_lowercase as alpha

counts = {key: 0 for key in alpha}

user_input = input("Enter the message: ")

for char in user_input.lower():
    if char in alpha:
        counts[char] = counts[char] + 1

most_common = sorted(counts.items(), key=lambda item: item[1],reverse=True)[:6]

for total_count in most_common:
    letter, count = total_count
    print(f"{letter} -> {count}")