import React, { useEffect } from 'react';
import axios from 'axios';


const VoiceActivityDetection = (props) => {

    let startFlag = props.startFlag

    // const [audioChunks, setAudioChunks] = useState([]);

    console.log('VOD running');
  useEffect(() => {
    const main = async () => {
      // Check if the vad and ort objects are defined
    //   if (window.vad && window.ort ) {
    if (startFlag === true ) {
        const myvad = await window.vad.MicVAD.new({ 

           

            onSpeechStart: () => {
            console.log('listining  - started');
          } , 
          
          onSpeechEnd: (audio) => {
            console.log('listining - stoped')
            // setAudioChunks(audio);
            // Do something with `audio` (Float32Array of audio sample
            sendAudioToBackend(audio)
          },
        });

        myvad.start();
      } else {
        console.error('vad or ort object is not defined');
        
      }
    };

    main();
  }, [startFlag]);

    const sendAudioToBackend = async (int16Array) => {
        // const url = 'http://localhost:8000/conversions/';
        const post_url = `http://localhost:8000/test/conversions/`;
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        };
        // const data = {
        //     "audio": int16Array
        // };
        const arrayAsString = int16Array.join(', ');

        const data = {
            "audio": arrayAsString
        }

        console.log('from vod', data);
        console.log('from cod data type',typeof(data));
        // const response = await axios.post(post_url , data, { headers });
        // console.log('Response: from API', response.data);


        try {
            const response = await axios.post(post_url , data, { headers });
            console.log('Response:', response.data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

  return (
    <div>
      {/* Your component content */}
      

    </div>
  );
};

export default VoiceActivityDetection;
