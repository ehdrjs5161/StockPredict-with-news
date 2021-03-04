// import React, {useState, useEffect} from 'react';
// import axios from 'axios';
// import {LineChart, Line, YAxis, XAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
// import styles from '../App.css';

// class Company extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       code: "",
//       name: "",
//       predict_day1: 0,
//       predict_rate1: 0,
//       predict_day7: [],
//       predict_rate2: [],
//       price: [{}],
//       price_day1: [{}],
//       price_day7: [{}]
//     }
//   }

//   componentDidMount() {
//     this.getPrice();
//     this.getPriceDay1();
//     this.getPriceDay7();
//   }

//   getPrice(){
//     fetch(`/code=${this.state.code}`).then(res=>{
//         if(res.status != 200){
//             throw new Error(res.statusText);
//         }
//         return res.json();
//     }).then(price => this.setState({price}));
//   }

//   componentWillUnmount() {

//   }

//   render() {
//       return (
//           <div>
//               <h1>{this.state.code}</h1>
//               <h2>{this.state.name}</h2>
//           </div>
//       )
//   }
// }
// //   componentDidMount(){
// //     this.getCode();
// //     this.getName();
// //     this.getResult_day1();
// //     this.getResult_day7();
// //   }

// //   getCode() {
// //     fetch('${apiURL}/code=${this.props.match.params.code}.json').then(res => {
// //       if(res.status != 200){
// //         throw new Error(res.statusText);
// //       }
// //       return res.json();
// //     }).then(code =>this.setState())
// //   }
// // }

// export default Company;