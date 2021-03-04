import { React, useEffect, useState, Component } from 'react';
import { rate } from '../Components/Rate';

function Rank() {
  const [data, setData] = useState([{}]);
  
  useEffect(() => {
    fetch('/rank').then(
      response => response.json([])
    ).then(data=>setData(data))
  },[{}]);

  console.log(rank);
  return(
    <div>
      <h1>아이 싯팔!</h1>
    </div>
  );
 }

export default Rank;