import pandas as pd

columns = ['sessionid', 'audiodata', 'textdata']
df = pd.DataFrame(columns=columns)

def sendatatodataframe(id, audio, text):
    df.empty()
    new_row = pd.DataFrame({'sessionid': [id], 'audiodata': [audio], 'textdata': [text]})
    df = pd.concat([df, new_row], ignore_index=True)
    return df


# Sample data

audio = [0.1, -0.2, 0.3]
text = ["hello", "world", "example"]

# Call the function to add a new row
# df = sendatatodataframe(f'AUD{counter:03d}', audio, text, df)

# # Sample data for the second call
# audio2 = [0.4, 0.5, -0.6]
# text2 = ["data", "example", "test"]

# # Call the function again to add a new row with different data
# df = sendatatodataframe(f'AUD{counter:03d}', audio2, text2, df)

# Sample data for the third call
id = 4
audio4 = [0.7, 0.8, 0.9]
text4 = ["more", "data", "here"]

# Call the function again to add a new row with different data
df = sendatatodataframe(id,  audio4, text4)

print(df)
