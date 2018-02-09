
def which_prize(point):
    prize = None
    if point >= 0 and point <= 50:
        prize = "wooden rabbit"
    elif point >= 51 and point <= 150:
        prize = None
    elif point >= 151 and point <= 180:
        prize = "wafer-thin mint"
    elif point >= 181 and point <= 2000:
        prize = "penguin"

    if prize:
        return "Congratulations! You have won a " + prize + "!"
    else:
        return "Oh dear, no prize this time."


print(which_prize(0))
print(which_prize(51))
print(which_prize(151))
print(which_prize(181))
