import asyncio
import nest_asyncio
nest_asyncio.apply()
async def a():
    print("suspend a")
    await asyncio.sleep(2)
    print("resume a")
    return "a"
async def b():
    print("suspend b")
    await asyncio.sleep(2)
    print("resume b")
    return "b"

return_value_a,return_value_b = await asyncio.gather(a(),b())
return_value_a,return_value_b