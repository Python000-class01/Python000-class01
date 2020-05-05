import time


def to_date_time(time_dis):
    now = time.time()
    print(now)
    if time_dis.find('秒') > 0:
        count = time_dis.split('秒')[0]
        now = now - 1 * int(count)
    if time_dis.find('分') > 0:
        count = time_dis.split('分')[0]
        now = now - 60 * int(count)
    if time_dis.find('时') > 0:
        count = time_dis.split('小时')[0]
        now = now - 3600 * int(count)
    if time_dis.find('天') > 0:
        count = time_dis.split('天')[0]
        now = now - 86400 * int(count)
    if time_dis.find('月') > 0:
        count = time_dis.split('月')[0]
        now = now - 2592000 * int(count)
    if time_dis.find('年') > 0:
        count = time_dis.split('年')[0]
        now = now - 31536000 * int(count)
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
