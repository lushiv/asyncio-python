# Asynchronous For Python(asyncio)
asyncio is a library to write concurrent code using the async/await syntax.asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
asyncio is often a perfect fit for IO-bound and high-level structured network code.

## Asynchronous vs Synchronous
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/nRhyqYw/Screenshot-from-2022-01-31-23-20-39.png" height="175px"/></a>

### Synchronous Hello World! Example:-


  ```
  def main():
  print("Hello")

main()
print("World")


  ```

###  Asynchronous Hello World! Example :


```
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())

```

## Asyncio Event Loop:
The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/9tFMBcr/470771-1-En-2-Fig1-HTML.jpg" height="175px"/></a>

## Async/Await Keywords


## Tasks


# Coroutine :
Coroutines are computer program components that generalize subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed. ... According to Donald Knuth, Melvin Conway coined the term coroutine in 1958 when he applied it to the construction of an assembly program.

```
send() — used to send data to coroutine
close() — to close the coroutine
```

<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/d2p2PW1/Screenshot-from-2022-02-02-23-10-25.jpg" height="175px"/></a>
