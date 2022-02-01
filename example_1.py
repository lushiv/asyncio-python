import  asyncio

async def fun_1():
    print("*****************Started*********************")
    print("hello")

    await fun_2("World")
    task = asyncio.create_task(fun_2("********* Print After the Finished *********"))

    # await task 
    await asyncio.sleep(15) # waiting for 15 sec response from task
    print("*****************Finished*********************")


async def fun_2(value):
    print(value)
    await asyncio.sleep(1)

asyncio.run(fun_1())