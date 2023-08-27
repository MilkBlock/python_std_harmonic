# import asyncio
# async def main():
#     await asyncio.sleep(1)
#     print('hello')
# with asyncio.Runner as r:
#     r.run
import types
import itertools
import asyncio
import nest_asyncio
nest_asyncio.apply()

async def counter(name: str):
    for i in range(0, 100):
        print(f"{name}: {i!s}")
        await asyncio.sleep(0)

async def main():
    tasks = []
    for n in range(0, 4):
        tasks.append(asyncio.create_task(counter(f"task{n}")))
    while True:
        tasks = [t for t in tasks if not t.done()]
        if len(tasks) == 0:
            return
        await tasks[0]

# t : asyncio.Task = asyncio.create_task(main())
# asyncio.
from itertools import *
c = count(5)
for i in range(52):
    print(c.__next__())

itertools.islice()
itertools.combinations_with_replacement()
itertools.combinations()
import functools
itertools.islice()