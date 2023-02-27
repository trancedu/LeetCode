import asyncio 
import time 

async def call_api(name: str, delay: float):
    print(f"{name} - step 1")
    await asyncio.sleep(delay)
    print(f"{name} - step 2")
    return f"{name} completed"
    
async def main():
    print("Main Thread Start")
    start = time.time()
    # 先创建task，再await task，这样可以并行执行
    task1 = asyncio.create_task(call_api("A", 1))
    task2 = asyncio.create_task(call_api("B", 0.5))
    
    await task1 
    print("Task1 Finished")
    await task2
    print("Task2 Finished")
    
    print("Main Thread End")
    print(f"Total time: {time.time() - start}")

async def my_gather():    
    results = await asyncio.gather(
        call_api("A", 1),
        call_api("B", 0.5)
    )
    print(results)
    
if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(my_gather())
