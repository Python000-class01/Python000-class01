import aiohttp
import asyncio

url = 'http://httpbin.org/get'


async def fetch(client, url):
    # get 方式请求url
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    # 获取session对象
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, url)
        print(html)


loop = asyncio.get_event_loop()  # 创建事件循环
task = loop.create_task(main())  # 把需要做的事情的函数和事件绑定
loop.run_until_complete(task)   # 运行
# Zero-sleep 让底层连接得到关闭的缓冲时间
loop.run_until_complete(asyncio.sleep(0))
loop.close()
