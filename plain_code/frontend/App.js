import logo from './logo.svg';
import './App.css';
import './ComponentsfirstPage/gameButtonComponent'
import ButtonsMenu from "./ComponentsfirstPage/selectGameComponent"
import'./ComponentsfirstPage/levelButtonsComponent'
import SudokuBoard from "./ComponentsSecondPage/SudokuBoardComponent";

import axios from 'axios';
import React, { useState } from "react";
import FirstPage from "./ComponentsfirstPage/FirstPage";
import SecondPage from "./ComponentsSecondPage/SecondPage";


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
    };

render() {
        return (
            <div className="App">
                {this.state.currentPage === 1 && (
                    <div>
                        {/* Content of the first page */}
                        <FirstPage onSelectLevel={this.onSelectLevel}/>
                    </div>
                )}

                {this.state.currentPage === 2 && (
                    <div>
                        {/* Content of the second page */}
                        <SecondPage/>
                    </div>
                )}
            </div>
        );
    }
}

export default App;
