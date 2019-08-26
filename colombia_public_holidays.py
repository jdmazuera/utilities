def getPascua(year):
    from datetime import date
    from dateutil.relativedelta import relativedelta

    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (13 + 8 * k) // 25
    q = k // 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19 * a + M) % 30
    e = (2 * b + 4 * c + 6 * d + N) % 7

    if d + e < 10:
        start_date = date(year,3,(22 + (d + e)) )
        return start_date
    else:
        start_date = date(year,4,((d+e)-9))
        return start_date

def getPublicHolidaysOfYear(year):
    """
    Receives a date object and validate if it is a public holiday or not
    date = Date Object Python
    """
    from datetime import date
    from dateutil.relativedelta import relativedelta

    # Add public holiday here when is a fixed day

    fixed_public_holidays = [
        date(year,1,1),
        date(year,5,1),
        date(year,7,20),
        date(year,8,7),
        date(year,12,8),
        date(year,12,25)
    ]

    # Add public holiday here when is located on monday but can be move if the day is not a monday in base date

    not_fixed_public_holidays = [
        date(year,1,6),
        date(year,3,19),
        date(year,6,29),
        date(year,8,15),
        date(year,10,12),
        date(year,11,1),
        date(year,11,11)
    ]

    for index,day in enumerate(not_fixed_public_holidays):
        if day.weekday() == 0:
            continue
        else:
            delta = 7 - day.weekday()
            not_fixed_public_holidays[index] = day + relativedelta(days=delta)

    holy_days = []

    pascua_deltas = [-3,-2,43,64,71]
    
    pascua_date = getPascua(year)

    for i in pascua_deltas:
        holy_days.append(
            (pascua_date + relativedelta(days=i))
        )

    public_holidays = fixed_public_holidays + not_fixed_public_holidays + holy_days

    public_holidays.sort()

    return public_holidays

def getPublicHolidays(years=[]):

    public_holidays = []

    for year in years:
        public_holidays += getPublicHolidaysOfYear(year)

    return public_holidays