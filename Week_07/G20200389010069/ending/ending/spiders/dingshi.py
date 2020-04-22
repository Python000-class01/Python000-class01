import os
import time
from scrapy import cmdline
import datetime
import time
import shutil
import os



if __name__ == '__main__':
 #os.system('pwd')
    while True:
        os.system("scrapy crawl movice")
#每２0s执行一次
        time.sleep(20)

from scrapy import cmdline
import datetime
import time
import shutil
import os

recoderDir = r"crawls"   # 这是为了爬虫能够续爬而创建的目录，存储续爬需要的数据
checkFile = "isRunning.txt"  # 爬虫是否在运行的标志

startTime = datetime.datetime.now()
print(f"startTime = {startTime}")

i = 0
miniter = 0
while True:
    isRunning = os.path.isfile(checkFile)
    if not isRunning:                       # 爬虫不在执行，开始启动爬虫
        # 在爬虫启动之前处理一些事情，清掉JOBDIR = crawls
        isExsit = os.path.isdir(recoderDir)  # 检查JOBDIR目录crawls是否存在
        print(f"mySpider not running, ready to start. isExsit:{isExsit}")
        if isExsit:
            removeRes = shutil.rmtree(recoderDir)  # 删除续爬目录crawls及目录下所有文件
            print(f"At time:{datetime.datetime.now()}, delete res:{removeRes}")
        else:
            print(f"At time:{datetime.datetime.now()}, Dir:{recoderDir} is not exsit.")
        time.sleep(20)
        clawerTime = datetime.datetime.now()
        waitTime = clawerTime - startTime
        print(f"At time:{clawerTime}, start clawer: mySpider !!!, waitTime:{waitTime}")
        cmdline.execute('scrapy crawl mySpider -s JOBDIR=crawls/storeMyRequest'.split())
        break  #爬虫结束之后，退出脚本
    else:
        print(f"At time:{datetime.datetime.now()}, mySpider is running, sleep to wait.")
    i += 1
    time.sleep(600)        # 每10分钟检查一次
    miniter += 10
    if miniter >= 1440:    # 等待满24小时，自动退出监控脚本
        break




















# flag = 0
#     # 获取当前时间
# now = datetime.datetime.now()
#     # 启动时间
#     # 启动时间为当前时间 加5秒
# sched_timer = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute,
#                                     now.second) + datetime.timedelta(seconds=5)
#     # 启动时间也可自行手动设置
#     # sched_timer = datetime.datetime(2017,12,13,9,30,10)
# while (True):
#         # 当前时间
#     now = datetime.datetime.now()
#         # print(type(now))
#         # 本想用当前时间 == 启动时间作为判断标准，但是测试的时候 毫秒级的时间相等成功率很低 而且存在启动时间秒级与当前时间毫秒级比较的问题
#         # 后来换成了以下方式，允许1秒之差
#     if sched_timer < now < sched_timer + datetime.timedelta(seconds=1):
#         time.sleep(1)
#         print(now)
#             # 运行程序
#         main(sched_timer)
#             # 将标签设为 1
#         flag = 1
#     else:
#             # 标签控制 表示主程序已运行，才修改定时任务时间
#         if flag == 1:
#                 # 修改定时任务时间 时间间隔为2分钟
#             sched_timer = sched_timer + datetime.timedelta(minutes=60)
#             flag = 0
