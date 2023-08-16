import pandas as pd

# cnames=['sessionid' , 'audiodata', 'textdata']
# df = pd.DataFrame(columns=cnames)
# df.to_csv('maindataframe.csv', index=False)

# df = pd.read_csv('maindataframe.csv')
# df['audiodata'].astype('float32').dtypes
# df['textdata'].astype('str').dtypes


import pandas as pd

df = pd.read_csv('maindataframe.csv')
counter = 1

def sendatatodataframe(counter, audio, text, df):
    
    session_id = f'AUD{int(counter):03d}'
    new_row = pd.DataFrame([[session_id, audio, text]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    counter += 1
    return counter, df





counter = 1
audio = [1, 135555326465412, 6546546]
text = ["dasdasasl;dfhal;ksdfj;aslkj"]
counter, df = sendatatodataframe(counter, audio, text, df)
print(df)
