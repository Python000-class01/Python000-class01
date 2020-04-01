学习笔记
#迭代器
1、迭代器为字典类型的，一但生成， 在对迭代器插入会损坏迭代器
2、尾插入的列表迭代器，不会顺坏当前list迭代器，列表会自动变长
3、迭代器一旦耗尽，永久损坏
# 协程
1、send 可以发送值给协程 yield 关键字
2、3.5版本以上 要使用协程，方法前面都要加 async，实现协程，使用关键字 await
3、async和await 是一组，await 必须在函数使用
如：python3.5版本 增加async await

def sth():
    pass
async def py35_func():
    await sth()
       
# 注意：
 await 接收的对象必须是awaitable对象
 awaitable 对象定义了__await__()方法
 awaitable 对象有三类，使用多个协程 可以使用 Task
 1 协程 coroutine
 2 任务 Task
3 未来对象 Future 
4、使用协程， 需要引入 asyncio 库 
coroutine 使用实例：
async def main():
    print('hello')
    await asyncio.sleep(3)
    print('world')
协程不能直接 直接运行， 需要交给 asyncio.run() 执行
 asyncio.run()运行最高层级的conroutine
asyncio.run(main())

#Task 使用实例1
async 函数被调用后会创建一个coroutine
 这时候该协程并不会立即运行，
 需要通过 ensure_future 或 create_task 方法生成 Task 后才会被调度执行
async def mission(time):
    await asyncio.sleep(time)


async def main():
    start_time = time.time()
    # asyncio.create_task()封装成task，函数用来并发运行作为 asyncio 任务 的多个协程
    tasks = [asyncio.create_task(mission(1)) for proxy in range(10000)]  # 创建1w个协程
    [await t for t in tasks]
    print(time.time() - start_time)


if __name__ == "__main__":
    asyncio.run(main())
    
    
    
Task 使用实例2
import asyncio
import time

async def coroutine_child1_demo():
    await asyncio.sleep(2)
    return 1


async def coroutine_child2_demo():
    await asyncio.sleep(5)
    return 2


tasks = [
    coroutine_child1_demo(),
    coroutine_child2_demo()
]

if __name__ == "__main__":
    start = time.time()  # 开始时间

    ioloop = asyncio.get_event_loop()  # 创建事件循环ioloop
    coroutine = asyncio.wait(tasks)  # 启动协程
    # Future 是一种特殊的 底层级 可等待对象，表示一个异步操作的 最终结果
    future = asyncio.ensure_future(coroutine)  # 封装成一个future对象
    ioloop.run_until_complete(future)  # 提交给ioloop,等future对象完成
    ioloop.close()  # 不进行ioloop读写要关闭

    # debug
    print(future.done())  # 协程任务是否完成
    print(future.result())  # 协程任务执行的结果

    end = time.time()  # 结束时间

    print(str(end - start))
    
    
# ansible 

# pandas 学习

1、pandas 读取文件后， 默认自动添加索引  
2、pandas.Series  为一维数据
3、import pandas as pd  
s1 = pd.Series({'a':11, 'b':22, 'c':33})
 获取全部索引
s1.index
使用index会提升查询性能
如果index唯一，pandas会使用哈希表优化，查询性能为O(1)
如果index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)
如果index完全随机，每次查询都要扫全表，查询性能为O(N)
3、pandas.DataFrame 数据类似二维数据
4、pandas 数据导入