# SpeechtotextProject1
A application listens to user input and calls GCP speech to text api and saves audio and text data on postgres db

Clone this repo

cd speechtotextui


run 'npm install'


cd /src 


run 'npm start'


react app launches in 'http://localhost:3000/'


cd appbackend


create 'env' virtual enviornment



Activate the virtual env, 



run 'pip install -r requirments.txt'



SETUP GCP Speechtotext api , enable cloud api in 'API and services' and get 'key.json'
https://www.youtube.com/watch?v=lKra6E_tp5U {watch this to setup GCP speech to text api}




use your key.json



run cmd 'uvicorn main:app --reload'



FastAPI runs in 'http://127.0.0.1:8000/docs'


go to React app and Click button 'Start', 


VAD 'voice actication dectection' detects your voice from microphone , {allow microphone when app starts}


After listining stoped , UI makes Post request to FASTAPI with audiodata and Backend runs a GCP Speechtotext API to convert audio into text and backend returns 'textdata' to ui



console log will display the results



