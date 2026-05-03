win_letter, win_num = input().split()
buy_letter, buy_num = input().split()

def last_n_digits(num1, num2, n):
    return num1[-n:] == num2[-n:]

prize = 0

if win_letter == buy_letter and win_num == buy_num:
    prize = 1000000
elif win_num == buy_num:
    prize = 100000
elif win_letter == buy_letter and last_n_digits(win_num, buy_num, 3):
    prize = max(prize, 2000)
elif win_letter == buy_letter and last_n_digits(win_num, buy_num, 2):
    prize = max(prize, 1000)
elif win_letter != buy_letter and last_n_digits(win_num, buy_num, 3):
    prize = max(prize, 200)
elif win_letter != buy_letter and last_n_digits(win_num, buy_num, 2):
    prize = max(prize, 100)
elif win_letter == buy_letter:
    prize = max(prize, 20)

print(prize)
