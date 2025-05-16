import threading
import time

### Function for Threading ###

def example_function(string):
  print(string)

  print(time.perf_counter())

  time.sleep(2)
  print("Sleep Done")

  print(time.perf_counter())

### Single Thread ###

print("Single Thread Section Starting")

example_single_thread = threading.Thread(target=example_function, args=('example_arg',))

example_single_thread.start()

example_single_thread.join()

print("Single Thread Section Finished")

### Multiple Threads ###

print("Multiple Threads Section Starting")

arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']
emt = []

for i in arg_list:
    example_multiple_thread = threading.Thread(target=example_function, args = (i, ))
    emt.append(example_multiple_thread)

for i in emt:
  i.start()

for i in emt:
  i.join()

print("Multiple Threads Section Finished")