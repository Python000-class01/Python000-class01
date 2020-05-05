def get_nday_list(n):
    """最近 n 天
    今日 15 号：['2020-04-11', '2020-04-12', '2020-04-13', '2020-04-14', '2020-04-15']
    """
    import datetime
    before_n_days = []
    for i in range(0, n)[::-1]:
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    return before_n_days

def get_day_nday_ago(date,n):
    import datetime
    t = time.strptime(date, "%Y-%m-%d")
    y, m, d = t[0:3]
    Date = str(datetime.datetime(y, m, d) - datetime.timedelta(n)).split()
    return Date[0]
