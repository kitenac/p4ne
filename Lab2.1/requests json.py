import requests

r = requests.get('https://swapi.dev/api/' + 'people' + '/' + '1')

# content достать
res = r.content
print(f'response content: {res}')

# json str ---> dictionary
jsoned = r.json()
print(f'''
JSONed: {jsoned}\n
      name: {jsoned["name"]}
      height: {jsoned["height"]}
      hair: {jsoned["hair_color"]}
      ''')