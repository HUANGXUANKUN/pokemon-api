import json

with open('pokedex.json', 'rb') as f:
    data = json.load(f)
    # print(data)

output = []
base_url = "https://raw.githubusercontent.com/HUANGXUANKUN/pokemon-Api/master/images/"
high_1 = 0
high_2 = 0
high_3 = 0
high_4 = 0
high_5 = 0
high_6 = 0

for pokemon in data:
    output_s = {}
    output_s['id'] = pokemon['id']
    len_1 = len(str(abs(output_s['id'])))
    new_id = ""
    if len_1 == 1:
        new_id = '00' + str(output_s['id'])
    elif len_1 == 2:
        new_id = '0' + str(output_s['id'])
    else:
        new_id = str(output_s['id'])

    output_s['id'] = new_id

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

    if output_s['hp'] > high_1:
        high_1 = output_s['hp']

    if output_s['attack'] > high_2:
        high_2 = output_s['attack']

    if output_s['defense'] > high_3:
        high_3 = output_s['defense']

    if output_s['sp_attack'] > high_4:
        high_4 = output_s['sp_attack']

    if output_s['sp_defense'] > high_5:
        high_5 = output_s['sp_defense']

    if output_s['speed'] > high_6:
        high_6 = output_s['speed']


    url = ""
    # id_len = len(output_s['id'])
    id_len = len(str(abs(pokemon['id'])))

    if id_len == 1:
        url += '00' + str(pokemon['id']) + '.png'
    elif id_len == 2:
        url += '0' + str(pokemon['id']) + '.png'
    else:
        url += str(pokemon['id']) + '.png'

    output_s['url'] = base_url + url
    # print(output_s['url'])

    # print("id: {}".format(output_s['id']))
    # print("name: {}".format(output_s['name']))
    # print("type: {}".format(output_s['type']))
    output.append(output_s)

with open('pokemon_data.json', 'w') as f:
    json.dump(output, f)

print("hp: {}".format(high_1))
print("attack: {}".format(high_2))
print("defense: {}".format(high_3))
print("s attack: {}".format(high_4))
print("s defense: {}".format(high_5))
print("speed: {}".format(high_6))
