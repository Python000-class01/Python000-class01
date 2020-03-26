import threading


# 这个函数名可随便定义
def run(n):
    print("current task：", n)


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("thread 1",))
    t2 = threading.Thread(target=run, args=("thread 2",))
    t1.start()
    t2.start()

    #  同步   得到结果之前， 调用不会立即返回  ；异步 请求发出后， 调用方立即返回， 没有返回结果，通过回调函数得到实际结果 被调用方    消息通讯机制
    #  阻塞 ： 得到调用结果之前线程程序被挂起；  非阻塞：不能立即得到结果不会阻塞线程   调用方
