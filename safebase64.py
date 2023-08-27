# import urllib.parse
# urllib.parse.quote(r"https://mineralsteins.icu:8080/a37/auth-alipay")

import asyncio
import random
async def coro(tag):
    print(">", tag)
    await asyncio.sleep(random.uniform(0.5, 5))
    print("<", tag)
    return tag
async def m():
    # loop = asyncio.get_event_loop()  # get current event loop

    tasks = [coro(i) for i in range(1, 11)]

    print("Get first result:")
    finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in finished:
        print(task.result())
    print("unfinished:", len(unfinished))

    print("Get more results in 2 seconds:")
    finished2, unfinished2 = await asyncio.wait(unfinished, timeout=2)

    for task in finished2:
        print(task.result())
    print("unfinished2:", len(unfinished2))

    print("Get all other results:")
    finished3, unfinished3 = await asyncio.wait(unfinished2)

    for task in finished3:
        print(task.result())

    await asyncio.sleep(1)
    # loop.close()

asyncio.run(m())