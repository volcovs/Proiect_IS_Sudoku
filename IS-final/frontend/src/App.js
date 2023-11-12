import logo from './logo.svg';
import './App.css';
import './ComponentsfirstPage/gameButtonComponent'
import ButtonsMenu from "./ComponentsfirstPage/selectGameComponent"
import'./ComponentsfirstPage/levelButtonsComponent'
import SudokuBoard from "./ComponentsSecondPage/SudokuBoardComponent";

import axios from 'axios';
import React from 'react';


class App extends React.Component {

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1>PENTRU LUMI</h1>
                    <ButtonsMenu/>
                    <SudokuBoard></SudokuBoard>
                </header>

            </div>
        );
    }
}

export default App;
