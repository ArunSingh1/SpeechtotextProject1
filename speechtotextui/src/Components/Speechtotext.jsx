import React, { useState , useEffect}  from 'react'
import { Box, Button, Typography } from "@mui/material";

import VoiceActivityDetection from './VoiceDectection';
// import Test from './Test';
import NewVad from './NewVad';


function Speechtotext() {
    
    const [isActive, setIsActive] = useState(false);
    const [seconds, setSeconds] = useState(0);



    useEffect(() => {
      let timer = null;
      if(isActive){
        timer = setInterval(() => {
          setSeconds((seconds) => seconds + 1);
        }, 1000);
      }
      return () => {
        clearInterval(timer);
      };
    });


    let [buttonclickstate, setButtonclickstate]  = useState(false)


  return (
    <Box  m="20px" >
        <Typography variant='h5'>
            Speech to Text Recognition 
        </Typography>
        
        
        <Button onClick={()=>{
            setButtonclickstate(buttonclickstate = true)
            setIsActive(true)
            console.log(buttonclickstate);
        }}

       >
            Start
        </Button>
        <Button
        onClick={()=>{
            setButtonclickstate(buttonclickstate = false)
            console.log(buttonclickstate);
            // clearInterval(null)
            // isActive(false)
            setIsActive(false)
            setSeconds(0)
        }}
        >
            Stop
        </Button>
        


        {buttonclickstate === true ? 
            
            <Typography variant='h6'>
                    Listening.... {seconds} seconds
            
            </Typography> : null
            
           
        }

        {/* {buttonclickstate === true ? <VoiceActivityDetection startFlag = {buttonclickstate}></VoiceActivityDetection>: null}
        {console.log(buttonclickstate)} */}
 
        {buttonclickstate === true ? <NewVad startFlag = {buttonclickstate}></NewVad>: null}
        {console.log(buttonclickstate)}

        {/* {buttonclickstate === true ? <Test></Test>:null}  */}


    </Box>

  )
}

export default Speechtotext