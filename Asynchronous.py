import time
import asyncio

### Function for Asynchronous ###

async def example_function(string):
  print(string)

  print(time.perf_counter())

  await asyncio.sleep(2)
  print("Sleep Done")

  print(time.perf_counter())

### Single Function Call ###

print("Single Asynchronous Section Starting")

asyncio.run(example_function("example_arg"))

print("Single Asynchronous Section Finished")

### Multiple Function Calls ###

print("Multiple Asynchronous Section Starting")

async def main():
   
    arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']
    efl = []

    for i in arg_list:
        efl.append(example_function(i))

    await asyncio.gather(*efl)

asyncio.run(main())

print("Multiple Asynchronous Section Finished")