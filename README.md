# Asynchronous For Python(asyncio)
asyncio is a library to write concurrent code using the async/await syntax.asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
asyncio is often a perfect fit for IO-bound and high-level structured network code.

## Asynchronous vs Synchronous
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/nRhyqYw/Screenshot-from-2022-01-31-23-20-39.png" height="175px"/></a>

### Synchronous Hello World! Example:-


  ```
  def main():
  print('Hello World')

main()

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