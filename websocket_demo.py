import asyncio
import nest_asyncio
import websockets
from websocket import connect
from websockets import connect
nest_asyncio.apply()
async def hello(uri):
    async with websockets.(uri) as websocket:
        await websocket.send("Hello world!")
        while True:
            m =await websocket.recv()
            print(m)
a = "s"

asyncio.run(hello("ws://mineralsteins.icu:25566/chata/"))


import json
_data = json.dumps({"a":3,"b":4})
print(_data)

# class a:
#     __num = 3
#     def get_num(self):
#         return self.__num


# b:a = a()
# b.__num = 4 
# print(b.__num)

    
