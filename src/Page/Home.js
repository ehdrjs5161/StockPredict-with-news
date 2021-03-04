import React, {useState} from 'react';
import {Route} from 'react-router-dom';

const Home = () => {
    const [input, setInput] = useState('');
    const onChange = (e) => {
        setInput(e.target.value);
    };

    const goPage = (e) => {
        <Route path="/code/:value" componet={e.target.value}/>
    };

    return (
        <div className="App">
            <h1>Ant: Stock Predict Service</h1>
            <input onChange={onChange} value={input}/>
            <button onChange={goPage}>Search</button>
            <div>
                <p>result: {input}</p>
            </div>
        </div>
    );
};

export default Home;