if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    triangle.about()
    print("-------------------")
    print(" Su Mo Tu We Th Fr Sa")
    time = dt.date(2002, 11, 1)
    start = 0
    day = 1
    next_month = time.month + 1
    while start <= time.weekday():
        print("   ", end='')
        start += 1
    while time.month < next_month:
        print(f'{day:3}', end='')
        if time.weekday() == 5:
            print()
        time += dt.timedelta(days=1)
        day += 1