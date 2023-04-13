

class prac:
    
    def __init__(self):
        self.sample_str = 'My Name Is Choi'
        self.sample_list = ['i','m','Groot']

    
    # count meth

    def count_prac(self):
        try:
            string = self.sample_str.lower()        # 소문자로 변환
            print(self.sample_str)
            find_char = input('찾을 알파벳 :').lower()
            print(string.count(find_char))      # 입력한 str에서 find가 몇개 있는지 확인 
        except Exception as e:
            print(f'무언가 잘못 된 것 같다.{e}')
            
    def find_prac(self):
        try:
            string = self.sample_str.upper()        
            print(self.sample_str)
            find_char = input('찾을 알파벳 :').upper()
            print(string.find(find_char))          # 입력한 문자열의 위치 출력 없을경우 -1 출력
        except Exception as e:
            print(f'무언가 잘못 된 것 같다.{e}')
            
    def index_prac(self):
        try:
            string = self.sample_str.upper()        # 대문자 변환
            print(self.sample_str)
            find_char = input('찾을 알파벳 :').upper()
            print(string.index(find_char))
        except Exception as e:
            print(f'무언가 잘못 된 것 같다.{e}')      # except 를 발생시킴 valueError
            
    def join_prac(self):
        print(self.sample_list)
        print(" ".join(self.sample_list))



if __name__ == '__main__':
    my_prac = prac()
    # my_prac.count_prac()
    # my_prac.find_prac()
    my_prac.join_prac()
    