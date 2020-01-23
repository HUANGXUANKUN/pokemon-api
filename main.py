import json

with open('pokedex.json', 'rb') as f:
    data = json.load(f)
    # print(data)

output = []
base_url = "https://raw.githubusercontent.com/HUANGXUANKUN/pokemon-Api/master/images/"

for pokemon in data:
    output_s = {}
    output_s['id'] = pokemon['id']
    output_s['name'] = pokemon['name']['english']
    output_s['type'] = pokemon['type'][0]
    # output_s['type'] = ""
    # for a in pokemon['type']:
    #     output_s['type'] += a + ', '
    # output_s['type'] = output_s['type'][:-2]
    output_s['hp'] = pokemon['base']['HP']
    output_s['attack'] = pokemon['base']['Attack']
    output_s['defense'] = pokemon['base']['Defense']
    output_s['sp_attack'] = pokemon['base']['Sp. Attack']
    output_s['sp_defense'] = pokemon['base']['Sp. Defense']
    output_s['speed'] = pokemon['base']['Speed']

    url = ""
    # id_len = len(output_s['id'])
    id_len = len(str(abs(output_s['id'])))

    if id_len == 1:
        url += '00' + str(output_s['id']) + '.png'
    elif id_len == 2:
        url += '0' + str(output_s['id']) + '.png'
    else:
        url += str(output_s['id']) + '.png'

    output_s['url'] = base_url + url
    print(output_s['url'])

    # print("id: {}".format(output_s['id']))
    # print("name: {}".format(output_s['name']))
    # print("type: {}".format(output_s['type']))
    output.append(output_s)

with open('pokemon_data.json', 'w') as f:
    json.dump(output, f)
