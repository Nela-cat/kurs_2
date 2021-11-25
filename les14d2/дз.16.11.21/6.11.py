cities={
'Tokyo':{
    'country':'Japan',
    'population':'135 m.',
    'fact':'The cleanest city',

    },
'Seoul':{
    'country':'Korea',
    'population':'120 m.',
    'fact':'Capital of plastic surgery',

    },
'Paris':{
    'country':'France',
    'population':'56 m.',
    'fact':'capital of France',

    },
    }
for c, i in cities.items():
    print("*"*37)
    print(f"город {c}: ")
    nfor = f'country -{i["country"]} , population - {i["population"]}, fact -{i["fact"]} '
    print(f'Информаыия о городе : {nfor}')
