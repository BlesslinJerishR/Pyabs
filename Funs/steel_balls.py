import random


def balls(ball):
    if ball == 1:
        return "Seri, certain"
    elif ball == 2:
        return "Seri, lighta"
    elif ball == 3:
        return "Seri, vaipu iruku"
    elif ball == 4:
        return "Seri, pakalam"
    elif ball == 5:
        return "Seri, solren"
    elif ball == 6:
        return "Seri, apdiaa"
    elif ball == 7:
        return "Seri, seri"
    elif ball == 8:
        return "Seri, kekren"
    elif ball == 9:
        return "Seri, vaipilla raja"


r = random.randint(1, 9)
fortune = balls(r)
print(fortune)