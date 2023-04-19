"""

루틴 -> 프로세스 , 스레드 의 흐름

일반적-> 스레드의 흐름

서브 루틴 (subroutine)
    동기
    파이선 파일의 순차적인 실행
    
코 루틴 (coroutine)
    비동기
    동시 실행
    
    
"""

# def my_coroutine():
#     while True:
#         value = yield       
#         print('Received value:', value)

# # 코루틴 객체 생성
# co = my_coroutine()

# # 코루틴 실행 준비
# next(co)

# # 값을 보내기
# co.send('Hello, world!')

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()
# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3

# def my_coroutine():
#     while True:
#         x = yield
#         print('Received:', x)

# co = my_coroutine()
# next(co)

# co.send(10) # Received: 10
# co.send(20) # Received: 20
# co.send(30) # Received: 30

"""오늘의 과제"""

# phone_book = {"John":"123-4567", "Jane": "341-7546", "Max":"934-1374"}

# def search():
#     name = yield
#     while True:
#         if name in phone_book:
#             phone_number = phone_book[name]
#         else:
#             phone_number = "없음"
            
#         name = yield phone_number
        
#         # 코루틴 생성
# search_coroutine = search()
# next(search_coroutine)

# # 검색 예시
# result = search_coroutine.send("John")
# print(result)

# result = search_coroutine.send("Jane")
# print(result)

# result = search_coroutine.send("Sarah")
# print(result)       # 없음이 출력됨

"""
# asyncic 비동기 프로그래밍을 위한 라이브러리, 코루틴 이용
# await 기다리는  run 실행
# 어떤 데이터를 가져오는데에 기다림이 필요할떄
"""
# import asyncio
# import random

# async def fetch_data():
#     print("데이터를 가져오는 중...")
#     await asyncio.sleep(1) # 데이터를 가져오는데 1초가 걸린다고 가정
#     return random.randint(1, 100)

# async def main():
#     data = await fetch_data()
#     print(f"가져온 데이터: {data}")

# asyncio.run(main())
# # 여러 코루틴이 있을 때 그 코루틴이 병렬적으로 실행되면서 어떤 코루틴이 작업을 한 데이터가 필요한 코루틴이 그 코루틴이 작업을 끝낼 때 까지 실행 대기한다
