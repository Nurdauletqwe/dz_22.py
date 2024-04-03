# import os
# import requests
# import json
# if not os.path.exists('json_files'):
#     os.makedirs('json_files')
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# data = response.json()
# for i, post in enumerate(data):
#     filename = f'json_files/post_{i}.json'
#     with open(filename, 'w') as f:
#         json.dump(post, f)
#         print(f'Файл {filename} сохранен успешно.')