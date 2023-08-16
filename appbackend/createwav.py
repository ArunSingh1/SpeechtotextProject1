import wave
import struct
import numpy as np
# Define your audio data as a list of floats


def create_wavfile(frames):
# Define output WAV file name
    WAVE_OUTPUT_FILENAME = 'newoutput.wav'

    # Define audio settings
    CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100  # Sampling rate in Hz

    data_array = np.array(frames)

    # Find the maximum absolute value in the data
    max_abs_value = np.max(np.abs(data_array))

    # Scale the data within the range of -1.0 to 1.0

    scaled_audio = data_array / max_abs_value



    # Pack the float audio data using struct
    data = struct.pack('f' * len(scaled_audio), *scaled_audio)

    # Create and configure the WAV file
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(4)  # 32-bit float audio data
    waveFile.setframerate(RATE)

    # Write the packed data to the WAV file
    waveFile.writeframes(data)

    # Close the WAV file
    waveFile.close()

    print('44100 wav file created')


import scipy.io.wavfile as wavfile
def create_wavfile(audio_samples):

    output_filename = '16000newoutput.wav'
    sample_rate = 16000
    audio_array = np.array(audio_samples, dtype=np.float32)
    
    # Scale the audio samples within the range of -1 to 1
    audio_array = np.clip(audio_array, -1.0, 1.0)
    
    # Scale the audio samples to the range of int16
    scaled_audio = np.int16(audio_array * 32767)
    
    
    # Save the WAV file
    wavfile.write(output_filename, sample_rate, scaled_audio)  
    print('16000 wav file created')   