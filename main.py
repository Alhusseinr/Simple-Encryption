import pandas as pd

encryptionkey = pd.read_csv(r"decodekeynew.csv", sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


def split(message):
    return [char for char in message]


message = 'your message here'
message_split = split(message)


def code_msg():
    coded_msg = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]

        except:
            print('unrecognized character')
            coded_char = '@@@'

        coded_msg = coded_msg + coded_char
    return coded_msg


coded_message = code_msg()
print(code_msg(), '\n')


def decoded_msg(message):
    new_word = ''
    decoded_msg = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]
        df2 = index_nb['Character'].tolist()
        s = [str(x) for x in df2]
        decoded_msg = decoded_msg + s
    new_word = ''.join(decoded_msg)
    return new_word


coded_message_str = str(coded_message)
print(decoded_msg(coded_message_str))
