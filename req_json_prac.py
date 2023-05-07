import requests
import json

data = {
        'title': 'homework', 
        'body': 'JY Choi', 
        'userId': 1
    }

def request_json(data:dict):
    '''
        과제 안내
        1. 파이썬코드를이용해아래와같은형태의JSON 데이터를body로삼아하단url로request 요청을보내주세요.
        {'title': ‘homework', 'body': ‘<자신의영문이름>', 'userId': 1}
        https://jsonplaceholder.typicode.com/posts
        2. 결과에서title, body, userId, id의값들만을파싱하여각기다른변수에담아주세요.
        3. 각변수에담은값들을result.txt에저장해주세요.
    '''
    response = requests.post('https://jsonplaceholder.typicode.com/posts',data)
    # print(json.loads(response.text))      # res json to dict
    data_dict = json.loads(response.text)
    title = data_dict['title']
    body = data_dict['body']
    userId = data_dict['userId']
    _id = data_dict['id']
    
    # print(title,body,userId,_id)          # check vars
    
    with open('result.txt', 'w') as fp:
        fp.write(title)
        fp.write(body)
        fp.write(userId)
        fp.write(str(_id))
    
    
if __name__ == '__main__':
    request_json(data)
