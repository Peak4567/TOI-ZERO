card_input = input().upper()

if len(card_input) == 2:
    rank = card_input[0]
    suit = card_input[1]
elif len(card_input) == 3:
    rank = card_input[0:2]
    suit = card_input[2]
    
if rank == 'A':
    rank_name = "ace"
elif rank == 'J':
    rank_name = "jack"
elif rank == 'Q':
    rank_name = "queen"
elif rank == 'K':
    rank_name = "king"
elif rank.isdigit() and 2 <= int(rank) <= 10:
    rank_name = rank

if suit == 'D':
    suit_name = "diamonds"
elif suit == 'H':
    suit_name = "hearts"
elif suit == 'S':
    suit_name = "spades"
elif suit == 'C':
    suit_name = "clubs"
else:
    print("กลุ่มไพ่ไม่ถูกต้อง")
    exit()

# แสดงผลชื่อไพ่
print(f"{rank_name} of {suit_name}")