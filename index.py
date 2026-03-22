#create Key Strings
#Autogenerate the value string by offsetting original string
#Create two dictionaries(one for enccoding and one for decoding)
#User input the message and mode[Encrypt/Decrypt]
#Return result


def crypto_light():
    keys ='abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
    msg = input("Enter your secret message: ")
    mode = input('Crypto mode: encode (e) OR decode as default ')
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    return new_msg.capitalize()        

print(crypto_light())   