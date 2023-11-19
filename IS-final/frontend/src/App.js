import logo from './logo.svg';
import './App.css';
import './ComponentsfirstPage/gameButtonComponent'
import ButtonsMenu from "./ComponentsfirstPage/selectGameComponent"
import'./ComponentsfirstPage/levelButtonsComponent'
import SudokuBoard from "./ComponentsSecondPage/SudokuBoardComponent";

import axios from 'axios';
import React from 'react';
import FirstPage from "./ComponentsfirstPage/FirstPage";
import SecondPage from "./ComponentsSecondPage/SecondPage";


class App extends React.Component {

    render() {
        return (
            <div className="App">
                    <SecondPage/>

            </div>
        );
    }
}

export default App;
