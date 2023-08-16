from fastapi import FastAPI,  Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List,  Union
from pydantic import BaseModel
import numpy as np

from scripts.createwav import create_wavfile, create_new

app = FastAPI(debug=True)

class AudioData(BaseModel):
    audio: List[int]


class NpaudioData(BaseModel):
    audio: str 

class newList(BaseModel):
  sections_to_consider: List[int]

origins = [
    "http://localhost:3000",  # Replace with the actual URL of your frontend
]

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods like "GET", "POST", etc.
    allow_headers=["*"],  # You can specify specific headers here
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/conversions/")
async def audio_array(audioData:AudioData):
    # received_audio = audio_data.audio
    # print(received_audio)
    print(audioData)
    print(type(audioData))
    return {"message": "Audio Array received"}


@app.post("/query/conversions/")
async def audio_array(feed: List[int] = Query(...)):
    return feed


@app.post("/test/conversions/")
async def audio_array(npaudioData:NpaudioData):
    # print(npaudioData)
    # print(npaudioData.audio)
    # print(type(npaudioData.audio))
    input_string = npaudioData.audio
    integer_list = [float(x.strip()) for x in input_string.split(',')]

    # output_filename = 'output.txt'

    # with open(output_filename, 'w') as file:
    #     for item in integer_list:
    #         file.write(str(item) + '\n')

    # print(integer_list)
    create_wavfile(integer_list)
    create_new(integer_list)


    
    
    return {"message": "Audio Array received"}