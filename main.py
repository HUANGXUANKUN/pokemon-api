import json

with open('pokedex.json', 'rb') as f:
    data = json.load(f)
    # print(data)

output = []
for pokemon in data:
    output_s = {}
    output_s['id'] = pokemon['id']
    output_s['name'] = pokemon['name']['english']
    output_s['type'] = ""
    for a in pokemon['type']:
        output_s['type'] += a + ', '
    output_s['type'] = output_s['type'][:-2]
    output_s['hp'] = pokemon['base']['HP']
    output_s['attack'] = pokemon['base']['Attack']
    output_s['defense'] = pokemon['base']['Defense']
    output_s['sp_attack'] = pokemon['base']['Sp. Attack']
    output_s['sp_defense'] = pokemon['base']['Sp. Defense']
    output_s['speed'] = pokemon['base']['Speed']

    # print("id: {}".format(output_s['id']))
    # print("name: {}".format(output_s['name']))
    # print("type: {}".format(output_s['type']))
    output.append(output_s)

with open('data.json', 'w') as f:
    json.dump(output, f)
