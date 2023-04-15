

class prac:
    
    def __init__(self):
        self.sample_str = 'My Name Is Choi'
        self.sample_list = ['i','m','Groot']
        self.sample_nermeric = [7,3,8,1,4,9,1]
        self.sample_dict = {}
        self.sample_init_dict = {
            
            'sample_str':self.sample_str,
            'sample_list':self.sample_list,
            'sample_nermeric':self.sample_nermeric
            
            }
        

    #############################################################   string method
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
        print(f'합쳐진 문자열 :{",".join(self.sample_list)}')
        return ",".join(self.sample_list)       # 리스트의 각 원소들을 특정 문자열과 함께 합쳐져줌
        
    def replace_prac(self):
        print(self.sample_str.replace("Choi", input('당신의 이름을 입력 :')))   # 특정 문자열을 다른 문자열로 바꿔줌
            
    def split_prac(self, string):
        print(f'리스트로 나눠진 문자열 :{string.split(",")}')
    #############################################################   string method end
        
    #############################################################   list method
    def len_prac(self):
        print(f'리스트의 길이: {len(self.sample_list)}')

    def del_prac(self):
        deleted_list = self.sample_list
        print(deleted_list)
        del deleted_list[2]             # 3번쨰 원소의 값을 삭제
        print(deleted_list)
    
    def append_prac(self):
        append_lsit = self.sample_list
        append_lsit.append('CHoi')      # 새로운 원소를 추가함
        print(append_lsit)
        
    def sort_prac(self):
        # print(id(self.sample_list))
        # print(id(self.sample_nermeric))
        
        print(self.sample_nermeric)
        print(sorted(self.sample_nermeric))     # 리스트의 원소에 직접적인 변형이 없이 정렬이됨
        self.sample_nermeric.sort()             # 리스트의 원소에 직접적인 변형이 발생
        print(self.sample_nermeric)
        
    def reverse_prac(self):
        print(f'{self.sample_nermeric}소팅전')
        self.sample_nermeric.reverse()                  # 리스트를 내림차 순으로 정렬함
        print(f'{self.sample_nermeric}리버스 소팅후')
    
    def index_prac(self):
        print(f'{self.sample_list}찾을 문자 입력')
        print(f'{self.sample_list.index(input())}')        # 리스트의 원소의 순번을 리턴함 
        print(self.sample_list.index('l'))              # 에러를 발생시킴
        
    def insert_prac(self):
        print(self.sample_nermeric)
        print(f'몇번째에 넣을 껀가요?')   # 리스트에 데이터를 삽힙함 인자(위치, 넣을 데이터) 
        self.sample_nermeric.insert(int(input()),99)
        print(self.sample_nermeric)
        
    def delete_prac(self):
        print(self.sample_nermeric)
        print(f'무엇 삭제?')
        self.sample_nermeric.remove(int(input()))           # 리스트의 특정 원소 삭제
        print(self.sample_nermeric)
        
    def pop_prac(self):
        print(f'{self.sample_nermeric} 입력')
        print(self.sample_nermeric.pop(int(input())))       # 해당 인덱스의 요소를 추출,삭제함
        print(f'{self.sample_nermeric}')
        
    def count_prac(self):
        print(f'{self.sample_nermeric} 입력')
        print(self.sample_nermeric.count(int(input())))     # 특정한 데이터의 개수를 추출
        
    def extend_prac(self):
        print(f'{self.sample_nermeric}')
        self.sample_nermeric.extend(self.sample_list)
        print(f'extend{self.sample_nermeric}')
        print(f'plus{self.sample_nermeric+[self.sample_str]}')
         
    ########################################################## dict method
    
    def dict_init_prac(self):
        a = 10
        self.sample_dict = {'a':1,
                            'b':2,
                            'c':a,
                            'd':'str',
                            'e':[a,'b',1,{'a_1':3}],            # 여러가지 데이터 타입을 계속 집어넣을 수 있음.
                            'f':(a,10,'avc'),
                            }
        
        print(self.sample_dict)
    
    def insert_dict_prac(self):
        self.dict_init_prac = {'old':987}
        print(self.dict_init_prac)
        self.dict_init_prac['new'] = 1234                   # 새로운 kv 를 추가
        print(f'새로운 k, v {self.dict_init_prac}')
    
    def dleete_dict_prac(self):
        self.dict_init_prac = {'old':987,'new':1234}
        print(self.dict_init_prac)
        del self.dict_init_prac['old']                  # k 값으로 삭제
        print(f'삭제됨{self.dict_init_prac}')
    
    
    def find_VbK_dict_prac(self):
        print(self.sample_init_dict)                    # k 값으로 v추출
        print(self.sample_init_dict['sample_str'])
        
    def ext_k_dict_prac(self):
        print(self.sample_init_dict.keys())             # k 추출
        print(list(self.sample_init_dict.keys()))       # k listfy
    
    def ext_v_dict_prac(self):
        print(self.sample_init_dict.values())             # v 추출
        print(list(self.sample_init_dict.values()))       # v listfy
        
    def dict_to_tuple_list_prac(self):
        print(self.sample_init_dict.items())            # dict 의 kv 를 tuple list 화
    
    def clear_dict(self):
        print(self.sample_init_dict)
        self.sample_init_dict.clear()               # dict의 모든 kv 를 삭제
        print(self.sample_init_dict)
        
    def get_dict(self):
        print(self.sample_init_dict.get('sample_str'))      # k 의 v 를 추출 직접적으로 데이터에 접근 하지 않아 이게 안전함 이것만 쓰세요
        print(self.sample_init_dict.get('my'))          # 해당 k 가 없으면 None 반환

    def in_dict(self):
        print('sample_str' in self.sample_init_dict )           # k가 있으면 true 없으면 false
        print('my' in self.sample_init_dict )          
        
        
    
    
if __name__ == '__main__':
    try:
        
        my_prac = prac()
        # my_prac.count_prac()
        # my_prac.find_prac()
        # my_prac.join_prac()
        # my_prac.replace_prac()
        # my_prac.split_prac(my_prac.join_prac())
        # my_prac.len_prac()
        # my_prac.del_prac()
        # my_prac.append_prac()
        # my_prac.sort_prac()
        # my_prac.reverse_prac()
        # my_prac.index_prac()
        # my_prac.insert_prac()
        # my_prac.delete_prac()
        # my_prac.pop_prac()
        # my_prac.count_prac()
        # my_prac.extend_prac()
        # my_prac.dict_init_prac()
        # my_prac.insert_dict_prac()
        # my_prac.dleete_dict_prac()
        # my_prac.find_VbK_dict_prac()
        # my_prac.ext_k_dict_prac()
        # my_prac.dict_to_tuple_list_prac()
        # my_prac.clear_dict()
        # my_prac.get_dict()
        my_prac.in_dict()
        
        
        
    except Exception as e:
        print(f'뭔가 빠진거 같아{e}')