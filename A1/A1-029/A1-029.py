text = input()

vowel_count = 0

if text[0] == 'a' or text[0] == 'e' or text[0] == 'i' or text[0] == 'o' or text[0] == 'u':
    vowel_count = vowel_count + 1

if text[1] == 'a' or text[1] == 'e' or text[1] == 'i' or text[1] == 'o' or text[1] == 'u':
    vowel_count = vowel_count + 1

if text[2] == 'a' or text[2] == 'e' or text[2] == 'i' or text[2] == 'o' or text[2] == 'u':
    vowel_count = vowel_count + 1

print(vowel_count)