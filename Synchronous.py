import time

### Function for Synchronous ###

def example_function(string):
  print(string)

  print(time.perf_counter())

  time.sleep(2)
  print("Sleep Done")

  print(time.perf_counter())

### Single Function Call ###

print("Single Synchronous Section Starting")

example_function("example_arg")

print("Single Synchronous Section Finished")

### Multiple Function Calls ###

print("Multiple Synchronous Section Starting")

arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']

for i in arg_list:
    example_function(i)

print("Multiple Synchronous Section Finished")