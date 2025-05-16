import multiprocessing
import time

### Function for MultiProcessing ###

def example_function(string):
  print(string)

  print(time.perf_counter())

  time.sleep(2)
  print("Sleep Done")

  print(time.perf_counter())

### Single Process ###

if __name__ == '__main__':

    print("Single Process Section Starting")
    example_single_process = multiprocessing.Process(target=example_function, args=('example_arg',))

    example_single_process.start()

    example_single_process.join()

    print("Single Process Section Finished")

### Multiple Process' ###

    print("Multiple Process' Section Starting")

    arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']
    emp = []


    for i in arg_list:
        example_multiple_process = multiprocessing.Process(target=example_function, args = (i, ))
        emp.append(example_multiple_process)

    for i in emp:
        i.start()

    for i in emp:
        i.join()

    print("Multiple Process' Section Finished")