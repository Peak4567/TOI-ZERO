n = int(input())
vowel_count = 0

for _ in range(n):
    ch = input().strip()
    if ch in ['A', 'E', 'I', 'O', 'U']:
        vowel_count += 1

print(vowel_count)
