import {useState} from 'react';

async function postRequest(url, data){
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json'},
    body: JSON.stringify(data),
  };

  let resp = await fetch(url, requestOptions).then(response => response.json())

  console.log(resp);

  return resp;
}

export default postRequest;