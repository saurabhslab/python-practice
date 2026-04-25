"""🧩 Problem 1: Say Hello Slowly
Write a program that:
waits 2 seconds
prints "Hello after 2 seconds"""
"""import asyncio

async def say_hello():
    print("This hello is very quick")
    await asyncio.sleep(10)
    print("This Hello is after 10 seconds")

asyncio.run(say_hello())"""

"""🧩 Problem 2: Two Messages
Make program that:
waits 1 second → prints "First"
waits 2 seconds → prints "Second"
💡 Hint:
Just call both functions one after another."""
"""
import asyncio

async def counting():
    await asyncio.sleep(5)
    print("First")
    await asyncio.sleep(10)
    print("Second")


asyncio.run(counting())"""

"""🧩 Problem 3: Run in Parallel

Create two async functions:

Task A → waits 2 sec → prints "A done"
Task B → waits 1 sec → prints "B done"

👉 Run them at the same time"""


import asyncio

async def task_A():
    await asyncio.sleep(1)
    print("A done")

async def task_B():
    asyncio.sleep(2)
    print("B done")

async def main():
     

