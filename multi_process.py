from multiprocessing import Process
import os

class Process_prac:
    
    def __init__(self):
        pass
    
    def pid_print(self):
        print(f'print pid: {os.getpid()} \n tip: pid 는 Process identifier (프로세스 식별자) 라고 한다. ')
        print(f'PID는 프로세스의 고유한 식별자입니다. 여러 os(ms, mac, unix)등 운영체제 커널에 사용되는 번호입니다.')
        answer = input("혹시 커널에 대해서 알고 싶나요?. YES == Enter")
        if answer != '':
            print(f'커널(Kernel)은 운영 체제의 일부로써 하드웨어와 프로세스의 운용을 위한 소프트웨어이다.')
            print('https://wikidocs.net/22368 확인')
        print(f'PID는 프로세스의 우선순위 조정, 종료 등 다양한 함수 호출에 사용됩니다.')
        
    def create_process(self):
        print(f'아이 Process 의 pid 는 {os.getpid()} 입니다.')
        print(f'이 아이의 부모 Process 의 pid 는 {os.getppid()} 입니다.')
        
    def kim(self):
        print('어이 김씨 창문 닦아')
        
    def lee(self):
        print('어이 이씨 바닥 쓸어')
        
    def park(self):
        print('어이 박씨 요리해')
        
if __name__ == '__main__':
    try:
        process_obj = Process_prac()
        # process_obj.pid_print()
        print(f'아부지 뭐하시노? {os.getpid()}인데요?')
        cd = Process(target=process_obj.create_process).start()
        cd2 = Process(target=process_obj.create_process).start()
        cd3 = Process(target=process_obj.create_process).start()
        # 프로세스 병렬 실행에 됨에 따라 create_process의 아이(자식) pid를 먼저 3번 출력한 뒤
        # 부모 pid를 3번 출력하게 된다.
        
        ex = Process(target=process_obj.kim).start()
        ex1 = Process(target=process_obj.lee).start()
        ex2 = Process(target=process_obj.park).start()
        
        
    except Exception as e:
        print(f'이런 저런 에러가 생긴거 같다. \n 그 오류는 다음과 같아: {e}')
    



