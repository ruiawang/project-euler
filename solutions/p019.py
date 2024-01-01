"""
We can use python datetime to find the day of week of any date in the range.
"""
import datetime

def solve():
    year = range(1901, 2001)
    month = range(1,13)
    return sum(1 for y in year for m in month if datetime.date(y,m,1).weekday() == 6)

if __name__ == "__main__":
    print(solve())