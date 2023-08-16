import os
from google.cloud import speech


def call_gcp_speechtotextapi():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speechtotext.json'
    speech_client = speech.SpeechClient()

    # audio_file = 'OSR_us_000_0010_8k.wav'
    audio_file = '16000newoutput.wav'

    with open(audio_file, 'rb') as f:
        audio_data = f.read()

    audio = speech.RecognitionAudio(content=audio_data)
    config_wav = speech.RecognitionConfig(
        language_code='en-US'

    )


    
    # more tan 1 min audio requires gcp cloud storage {gcs_uri} - gcp cloud storage url 

    # audio = speech.RecognitionAudio(uri=gcs_uri)
    # config = speech.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    #     sample_rate_hertz=44100,
    #     language_code="en-US",
    # )

    # operation = client.long_running_recognize(config=config, audio=audio)

    # print("Waiting for operation to complete...")
    # response = operation.result(timeout=90)



    response = speech_client.recognize(config = config_wav, audio=audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    print('GCP API Called')

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


# call_gcp_speechtotextapi()
