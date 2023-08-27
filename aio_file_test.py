import asyncio
import nest_asyncio
import aiofiles

async def read_file():
    async with aiofiles.open('data.txt', 'r') as file:
        contents = await file.read()
        print("nihao")
        print(contents)

async def main():
    await read_file()

nest_asyncio.apply()
asyncio.run(main())