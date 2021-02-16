import pandas as pd

encryptionkey = pd.read_csv(r"decodekeynew.csv", sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)
password = 'password'


def split(message):
    return [char for char in message]


def encode():
    encryptedPassword = ''
    passwordSplit = split(password)
    for i in range(len(passwordSplit)):
        j = passwordSplit[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]
        except:
            print('unrecognized character')
            coded_char = '@@@'

        encryptedPassword = encryptedPassword + coded_char
    return encryptedPassword


coded_password = encode()
print(encode())


def decoded_msg(password):
    decoded = []

    for i in range(0, len(password), 2):
        j = password[i:i + 2]
        index_nb = df[df.eq(j).any(1)]
        df2 = index_nb['Character'].tolist()
        s = [str(x) for x in df2]
        decoded = decoded + s
    new_word = ''.join(decoded)
    return new_word


print(decoded_msg(str(coded_password)))
