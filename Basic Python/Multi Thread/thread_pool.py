import time 
from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"{name} - step 1\n", end="")
    time.sleep(1)
    print(f"{name} - step 2\n", end="")
    return f"{name} completed"

with ThreadPoolExecutor() as executor:
    # if the task and arguments are different, we can use submit to run them in parallel
    result1 = executor.submit(task, "A")
    result2 = executor.submit(task, "B")

    print(result1.result()) # result() will wait for the task1 to finish
    print(result2.result()) # result() will wait for the task2 to finish

with ThreadPoolExecutor() as executor:
    # if the task is same, we can use map to run them in parallel
    results = executor.map(task, ["C", "D"])
    for result in results:
        print(result)