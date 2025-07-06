
def check_month(month: int):
    if month > 12 or month < 1:
        return 'Некорректный номер месяца'
    elif month == 12 or 1 <= month <= 2:
        return 'Зима'
    elif 3 <= month <= 5:
        return 'Весна'
    elif 6 <= month <= 8:
        return 'Лето'
    elif 9 <= month <= 11:
        return 'Осень'


def vote(votes):
    res = {}
    for v in votes:
        res[v] = votes.count(v)
    for key, value in res.items():
        if value == max(res.values()):
            return key


def discriminant(a, b, c):
    return (b**2) - (4*a*c)

def solution(a, b, c):
    d = discriminant(a, b, c)
    if d < 0:
        return 'корней нет'
    elif d == 0:
        return -1 * b / (2*a)
    else:
        x1, x2 = ((-1 * b + d**(1/2)) / 2 * a), ((-1 * b - d**(1/2)) / 2 * a)
        return x1, x2
