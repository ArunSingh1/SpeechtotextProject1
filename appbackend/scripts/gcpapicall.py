import os
from google.cloud import speech


counter = 1
def call_gcp_speechtotextapi():

    global counter

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speechtotext.json'
    speech_client = speech.SpeechClient()

    audio_file = 'OSR_us_000_0010_8k.wav'
    # audio_file = '16000newoutput.wav'

    with open(audio_file, 'rb') as f:
        audio_data = f.read()

    audio = speech.RecognitionAudio(content=audio_data)
    config_wav = speech.RecognitionConfig(
        language_code='en-US'

    )

    response = speech_client.recognize(config = config_wav, audio=audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    alltranscript = []
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        # print(f"Transcript: {result.alternatives[0].transcript}")
        alltranscript.append(result.alternatives[0].transcript)
        


    print(alltranscript)

    # alltranscript = ['I know you can pick my', " take my wife and you can't record this time"]

    print(len(alltranscript))
    if len(alltranscript) > 1:
        alltranscript = ' '.join(alltranscript)
        print(alltranscript)


    return alltranscript


call_gcp_speechtotextapi()
