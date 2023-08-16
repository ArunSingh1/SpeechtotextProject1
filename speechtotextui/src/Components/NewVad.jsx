
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Box, Button, Typography } from "@mui/material";



function NewVad(props) {

    const startFlag =  props.startFlag

    const [audioclips, setAudioclips] = useState([])


    console.log('from new', startFlag)
 

    useEffect ( ()=> {

        const vad_model = async () => {

            if (startFlag === true ) {

                const myvad = await window.vad.MicVAD.new({
                    
                    onSpeechStart: () => {
                        console.log('listining  - started');
                      } , 
                    
                    onSpeechEnd: (audio) => {
                    console.log('listining - stoped')

                    // addAudioClip(audio)
                    
                    sendAudioToBackend(audio)
                    },
                }
              
                )  
                myvad.start() 
                
                
                if (startFlag=== false){
                    myvad.stop()
                    
                }
                
            }


        }
        vad_model() 


    }, [startFlag])


    const addAudioClip = (newAudioArray) => {
        setAudioclips((prevAudioclips) => [...prevAudioclips, newAudioArray]);
        console.log(audioclips);
        console.log(typeof(audioclips));
      };
    
    const sendAudioToBackend = async (audioArray) => {
        // const url = 'http://localhost:8000/conversions/';
        const post_url = `http://localhost:8000/test/conversions/`;
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        };
        // const data = {
        //     "audio": int16Array
        // };
        const arrayAsString = audioArray.join(', ');

        const data = {
            "audio": arrayAsString
        }

        console.log('from vod', data);
        console.log('from cod data type',typeof(data));
        
        try {
            const response = await axios.post(post_url , data, { headers });
            console.log('Response:', response.data);
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

export default NewVad