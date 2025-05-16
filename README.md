# intro
this is as an educational walkthrough for me for the probably likely case where i forget how this stuff works if i spend time doing something unrelated in the future. because of this im writing this in a somewhat informal, very to the point way where i mention all the questions i'll have if things are forgotton. i figured the way it'll be written will be helpful to some of you, given it's the way i like first learning concepts instead of the hated but common occurence of chasing my tail in the deep end before figuring out where the starting point is. for this reason i've made it public.

as always, corrections in my code/descriptions/anything really are welcome.

# important stuff to know first
i've imported the time module, it's there so when different ways are used to run the same function you can see the effect, you should pay attention to this effect, you'll learn how each way works better. this doesn't need to be explained more right now, it's completely intuitive and you'll probably figure it out from examples before you even read the explanation for it. the learning process for each way is the same, mostly. it's going to involve showing a single function call and then many, and how things are handled.

there's two words you need to know too before you start reading, concurrency and coroutine. google ai says "concurrency in computing refers to the ability to handle multiple tasks or processes at the same time, either truly simultaneously or by interleaving them rapidly" and "a coroutine is a programming construct that allows a function to pause and resume its execution, enabling cooperative multitasking".

# normal function
this is our lab rat for synchronous, threading and multiprocessing. simple as ever and contains just enough to do what we need but no more.
```
def example_function(string):
  print(string)

  print(time.perf_counter())

  time.sleep(2)
  print("Sleep Done")

  print(time.perf_counter())
```
takes a string - prints the string - prints time - sleeps 2 seconds - prints sleep done - prints time  
note: read this againn, sounds (and is) simple but you forget one part to it and everything else gets confusing.

# synchronous
this is the one you're doing the whole time before you learn what concurrency is, it blocks the thread its running on meaning nothing else can be done on this thread untill it's finished.

## single function call:
```
example_function("example_arg")
```
nothing to say here really, as simple as it gets.

## output
Single Synchronous Section Starting  
example_arg  
74036.9174051  
Sleep Done  
74038.9184008  
Single Synchronous Section Finished

## multiple functions called:
```
arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']

for i in arg_list:
    example_function(i)
```
this is going to call the function with the next argument in the list each time. the next function won't be called untill the previous one is done.

## output
Multiple Synchronous Section Starting  
example_arg1  
74038.9197888  
Sleep Done  
74040.9210788  
example_arg2  
74040.9218514  
Sleep Done  
74042.9230254  
example_arg3  
74042.9239629  
Sleep Done  
74044.9251634  
example_arg4  
74044.9260313  
Sleep Done  
74046.9271687  
Multiple Synchronous Section Finished

# asynchronous
this is next step up from synchronous, an asynchronous function doesn't block the thread it's running on. this means that you run an async function inside an async function using ```await``` and that allows the async function to pause itself so other things can run.

## async function
```
async def example_function(string):
  print(string)

  print(time.perf_counter())

  await asyncio.sleep(2)
  print("Sleep Done")

  print(time.perf_counter())
```

same function as before, just different syntax to make it be used for asynchronous.

## single function call:
```
asyncio.run(example_function("example_arg"))
```

againn not much to say yet, just remember the syntax is different when dealing with an asynchronous function call.

## output
Single Asynchronous Section Starting  
example_arg  
74841.8003434  
Sleep Done  
74843.8069306  
Single Asynchronous Section Finished

## multiple functions called:
```
async def main():
   
    arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']
    efl = []

    for i in arg_list:
        efl.append(example_function(i))

    await asyncio.gather(*efl)

asyncio.run(main())
```

first off, notice you have to run an async function, you can't just do a bunch of function calls to an async function with different arguements each time.
```asyncio.gather(*efl)``` is used to group together the different cases of the function with different arguements each time and allow them to be ran concurrently, the ```*``` is used to unpack the ```efl``` list. you could await each function individually but they wouldn't be ran concurrently then.

## output
Multiple Asynchronous Section Starting  
example_arg1  
77622.8096829  
example_arg2  
77622.8100636  
example_arg3  
77622.8105148  
example_arg4  
77622.8108582  
Sleep Done  
77624.8247595  
Sleep Done  
77624.8255865  
Sleep Done  
77624.8263685  
Sleep Done  
77624.8271209  
Multiple Asynchronous Section Finished

notice from the time that when the sleep line gets hit the next function starts and everything is in order because unless paused, the running coroutine doesn't give way to something else untill it's done.

# threading
a thread is a unique flow of execution, they're useful because if one thread is waiting for something another one can run. priority depends on operating system scheduler.

## single function call:
```
example_single_thread = threading.Thread(target=example_function, args=('example_arg',))

example_single_thread.start()

example_single_thread.join()
```

syntax is obvious and the comma after ```'example_arg'``` isn't there by accident. ```start()``` creates the new thread and returns to main thread. join() stops the main thread from continuing untill the thread ```join()``` was called on is done.

## output
Single Thread Section Starting  
example_arg  
79583.1923672  
Sleep Done  
79585.1930145  
Single Thread Section Finished

## multiple functions called:
```
arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']
emt = []

for i in arg_list:
    example_multiple_thread = threading.Thread(target=example_function, args = (i, ))
    emt.append(example_multiple_thread)

for i in emt:
  i.start()

for i in emt:
  i.join()
```

## output
Multiple Threads Section Starting  
example_arg1  
79585.1943297  
example_arg2  
79585.1946822  
example_arg3  
79585.1951081  
example_arg4  
79585.1954027  
Sleep Done  
79587.1952059  
Sleep Done  
Sleep Done  
79587.1955066  
79587.1954338  
Sleep Done  
79587.1961021  
Multiple Threads Section Finished

notice the jumbled order, this is down to close timing in wake up times and how the operating system choses which thread goes next

# multiprocessing
a process is an independant program in execution, if one process is waiting on something another process can run. priority depends on operating system scheduler.

## single function call:
```
if __name__ == '__main__':

    print("Single Process Section Starting")
    example_single_process = multiprocessing.Process(target=example_function, args=('example_arg',))

    example_single_process.start()

    example_single_process.join()

    print("Single Process Section Finished")
```
if you run a script directly, ```__name__``` gets set to ```'__main__'```, if you create a child process from a parent process, the script is imported as a module. when imported as a module, ```__name__``` gets set to the module name. this means ```if __name__ == '__main__':``` will only allow whats underneath if the script is being called directly, which is what a parent program does.  ```start()``` and ```join()``` do the same things as in threading.

## output
Single Process Section Starting  
example_arg  
81182.8826127  
Sleep Done  
81184.8832869  
Single Process Section Finished

## multiple functions called:
```
if __name__ == '__main__':

    arg_list = ['example_arg1', 'example_arg2', 'example_arg3', 'example_arg4']
    emp = []


    for i in arg_list:
        example_multiple_process = multiprocessing.Process(target=example_function, args = (i, ))
        emp.append(example_multiple_process)

    for i in emp:
        i.start()

    for i in emp:
        i.join()
```


## output
Multiple Process' Section Starting  
example_arg1  
81185.1611447  
example_arg2  
81185.1762983  
example_arg3  
81185.1911413  
example_arg4  
81185.2098349  
Sleep Done  
81187.1620957  
Sleep Done  
81187.1770295  
Sleep Done  
81187.1920171  
Sleep Done  
81187.2108108  
Multiple Process' Section Finished

# final words
if you've made it this far i really appreciate it. to reiterate from earlier, i've probably gotten something wrong and would love to be told where, please do if you notice.   
would also appreciate any different interaction (saying interaction because there's definitely no such thing as likes on this platform and i lack a better word), even if being told on other social media platforms. i'd like to know that someone got help from this. given how much some of you have helped me, it's a small repayment on my societable debt.

see ya,  
3xpl0it
