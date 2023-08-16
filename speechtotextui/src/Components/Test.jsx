import React, {useEffect, useState} from 'react'
import axios from "axios";
function Test() {
    
    let URL = `http://localhost:8000/`
    const url = 'http://127.0.0.1:8000/conversions/';
    const headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    };
    const data = {
      "audio": [    -1051, 1829, -197, -2122, 3493, -3229, -302, 1906, -187, 4575, -1716, 847, 5124, -2101, -1470, 840, 1100, 2295, -3663, -5782, -1782, -4851, -563, 4073, 1470, 445, -3278, 1191, 4499, 2587, 1613, -1860, -786, -1413, -2760, 1223, 3685, 3713, 2563, -3672, -2400, 3237, 2076, 1574, -1598, -3859, -2437, -5869, -2689, 929, -1800, -2253, -2988, -451, 3037, 3410, 5462, 4541, 2668, 77, -2984, -744, 1402, -1040, -1937, -4659, -4209, -13, -578, 1197, 2643, 970, 145, -2262, -1772, 2213, 268]
  };

  console.log('working format', data);
  console.log('working format type', typeof(data));


    useEffect( ()=>{
        axios.get(URL).then((response)=>{
            console.log(response.data);

        });
    }, [URL])


    useEffect( ()=>{
      axios.post(url, data, { headers }).then((response)=>{

          console.log('post api', response.data);

      });
  }, [url])



  return (
    <div>Test</div>
  )
}

export default Test