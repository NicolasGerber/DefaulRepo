user = {}
def max_bid(bid_list):
    winner = ''
    maxbid = 0
    for n in bid_list:
        bid_amount = bid_list[n]
        if bid_amount > maxbid:
            maxbid = bid_amount
            winner = n
    print(f"The winner is {winner}, with the bid amount of ${maxbid}")


terminate = False
while terminate == False:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    user[name] = bid
    end = input("Are there any other person would like to Bid? (y/n): ").lower()
    print("\n" * 10)
    if end == 'n':
        terminate = True
max_bid(user)
