import asyncio
from queue import Queue

square_value = Queue()

async def calculate_square(number):
    print("**************Calculating square : {} ******************".format(number))
    await asyncio.sleep(3)
    print("Square of Number is : {} ".format(number*number))
    square_value.put(number*number)


async def calculate_cube(number):
    print("**************Calculating cube : {} ******************".format(number))
    await asyncio.sleep(3)
    print("Cuber of Number is : {} ".format(number * number * number))
    return number* number * number


async def main():

    # Create tasks
    task_1 = asyncio.create_task(coro=calculate_square(15))
    task_2 = asyncio.create_task(coro=calculate_cube(15))

    # await asyncio.wait_for(task_1,timeout=1)
    # await asyncio.sleep(1)

    await task_1

    while True:
        flag = square_value.empty()
        if flag:
            pass
        else:
            response = square_value.get()
            print(response)
            break


if __name__ == "__main__":
    asyncio.run(main())