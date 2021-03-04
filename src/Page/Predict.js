import React, {useState, useEffect} from 'react';
import {LineChart, Line, YAxis, XAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
import {Link} from 'react-router-dom';
import Rank from '../Components/Rank';
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";

function Predict ({match}) {
    const [inititalData, setinitialData] = useState([{
        code: "",
        name: "",
        predict_day1: 0,
        predict_day7: [{}],
        price_day1: [{}],
        price_day7: [{}],
        rate: {
            predict_rate1: 0,
            predict_rate2: []
        }
    }])
    
    useEffect(() => {
        fetch(`/code/${match.params.code}`).then(
        response =>response.json([])
        ).then(data=>setinitialData(data))
    },[]);

    const dataDay1 = inititalData['price_day1'];
    const dataDay7 = inititalData['price_day7'];
    const predictDay1 = inititalData['predict_day1'];
    const predictDay7 = inititalData['predict_day7'];
    
    return (
        <div>
            <h1>{inititalData.code} {inititalData.name}</h1>
            <ButtonGroup size="large" color="primary" aria-label="large outlined primary button group">
                <Button> 전체 가격</Button>
                <Button onClick={()=>{alert("hhhh")}}>1일 예측</Button>
                <Button onClick={()=> {alert("tttt")}}>7일 예측</Button>
            </ButtonGroup>
            <LineChart width={1200}
                height={500}
                data = {dataDay1}
            >
                <CartesianGrid strokeDasharray=""/>
                <YAxis yAxisId="right" orientation="right"/>
                <YAxis dataKey="Price"/>
                <XAxis dataKey="Date"/>
                <Tooltip/>
                <Legend/>
                <Line type="monotone" dataKey="Price" stroke="#8884d8" activeDot="r:8"/>
            </LineChart>
            <h1> 다음 개장일의 예측 가격은 {predictDay1}</h1>
        </div>
    )
}

export default Predict;