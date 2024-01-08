import logo from './logo.svg';
import './App.css';
import './ComponentsfirstPage/gameButtonComponent'
import'./ComponentsfirstPage/levelButtonsComponent'

import axios from 'axios';
import React, { useState } from "react";
import FirstPage from "./ComponentsfirstPage/FirstPage";
import SecondPage from "./ComponentsSecondPage/SecondPage";
import "./StylingFolder/PageStyle.css";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPage: 1,
        };
    }

    onSelectLevel = (selectedLevel, level) => {
        // Add logic to transition to the second page, for example:
        this.setState({ currentPage: selectedLevel});

        axios.post('http://localhost:8000/diffmsgs/', {msg: level})
            .then(r => console.log(r))
            .catch(err => console.log(err))
    };

    selectBack = () => {
        this.onSelectLevel(1, "Continue")
    }

render() {
        return (
            <div className="App">
                {this.state.currentPage === 1 && (
                    <div>
                        <FirstPage onSelectLevel={this.onSelectLevel}/>
                    </div>
                )}

                {this.state.currentPage === 2 && (
                    <div className="como">
                        <SecondPage/>
                        <button className={"game-button"} onClick={this.selectBack}>Back</button>
                    </div>
                )}
            </div>
        );
    }
}

export default App;
