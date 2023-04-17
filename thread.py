import threading
import os

class Thread_obj:
    def __init__(self):
        pass
    
    def create_thread(self):
        print(f'내 스레드 id {threading.get_native_id()}')
        print(f'내 pid {os.getpid()}')
    
    def kim(self):
        print('kim')
    def lee(self):
        print('lee')
    def park(self):
        print('park')
        
    
if __name__ == '__main__':
    my_thread = Thread_obj()
    
    print(f'나으 pid{os.getpid()}')
    
    new_thread = threading.Thread(target=my_thread.create_thread).start()
    new_thread2 = threading.Thread(target=my_thread.create_thread).start()
    new_thread3 = threading.Thread(target=my_thread.create_thread).start()
    
    new_new_thread = threading.Thread(target=my_thread.kim).start()
    new_new_thread2 = threading.Thread(target=my_thread.lee).start()
    new_new_thread3 = threading.Thread(target=my_thread.park).start()
    
        