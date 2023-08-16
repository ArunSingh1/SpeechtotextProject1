
import React, { useEffect } from 'react';
import axios from 'axios';
import { Box, Typography } from "@mui/material";



function VadModel(props) {

    const startFlag =  props.startFlag

    // const [audioclips, setAudioclips] = useState([])
    
    console.log('VAD Listining....')
 

    useEffect ( ()=> {

        const vad_model = async () => {

            if (startFlag === true ) {

                const myvad = await window.vad.MicVAD.new({
                    
                    onSpeechStart: () => {
                        console.log('listining  - started');
                      } , 
                    
                    onSpeechEnd: (audio) => {
                    console.log('listining - stoped')

                    // addAudioClip(audio)      the model sends packets of data whenever there was a longer pause,  
                                            // save to a usestate [] didnt work, so i handled the logic in backend , 
                                            // combines all the floats32 array into one and then proccessed it
                    
                    sendAudioToBackend(audio)
                    },
                }
              
                )  
                myvad.start() 
                
                
                if (startFlag=== false){
                    // myvad.stop()

                    myvad.pause()
                    
                }
                
            }


        }
        vad_model() 


    }, [startFlag])


    // const addAudioClip = (newAudioArray) => {
    //     setAudioclips((prevAudioclips) => [...prevAudioclips, newAudioArray]);
    //     console.log(audioclips);
    //     console.log(typeof(audioclips));
    //   };
    
    const sendAudioToBackend = async (audioArray) => {

        const post_url = `http://localhost:8000/conversions/`;
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        };
        // const data = {
        //     "audio": int16Array              FastAPI post didnt work with int64, headers failed 422 error, 
                                                // so input to send as str and changed in backend back to floats/ints
        // };
        const arrayAsString = audioArray.join(', ');

        const data = {
            "audio": arrayAsString
        }
       
        console.log('from vad-', data);
        console.log(post_url);

        try {
            const response = await axios.post(post_url , data, { headers });
            console.log('Response:', response.data);
            // console.log(response.data.textdata);

        } catch (error) {
            console.error('Error:', error);
        }
    };



  return (
    <Box>
        <Typography>
            App is running..
        </Typography>
       
    </Box>
  )
}

export default VadModel