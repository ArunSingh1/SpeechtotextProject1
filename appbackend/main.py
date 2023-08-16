from fastapi import FastAPI,  Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List,  Union
from pydantic import BaseModel
import numpy as np

from createwav import create_wavfile
from scripts.gcpapicall import call_gcp_speechtotextapi
# from scripts.senddatatodb import senddatato_db

app = FastAPI(debug=True)

# class AudioData(BaseModel):
#     audio: List[int]


class NpaudioData(BaseModel):
    audio: str 



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


# @app.post("/conversions/")
# async def audio_array(audioData:AudioData):
#     # received_audio = audio_data.audio
#     # print(received_audio)
#     print(audioData)
#     print(type(audioData))
#     return {"message": "Audio Array received"}





@app.post("/conversions/")
async def audio_array(npaudioData:NpaudioData):

    try:
        input_string = npaudioData.audio
        audio_list = [float(x.strip()) for x in input_string.split(',')]
        create_wavfile(audio_list)
        textdata =  call_gcp_speechtotextapi()

        
        # DB coonection failed 'for me' with wsl error, replace ip password and schema it will work
        # senddatato_db(audiodata=audio_list, textdata=textdata)
        res = {
            "message": "Sucess" ,
            "textdata": textdata[0]            
            }
    except:
        res = {
            "message": "error" ,
            "textdata": []   
        }



    
    return res