// SudokuBoard.js
import React, { Component } from "react";
import SudokuCell from "./SudokuCellComponent";
import axios from "axios";
import "../StylingFolder/SudokuBoardStyle.css"

class SudokuBoard extends Component {state = {details: [], }
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    constructor(props) {
        super(props);

        let data_game;

        axios.get('http://localhost:8000/board/')
            .then(res => {
                data_game = res.data;

                this.setState({
                    details: data_game,
                })

                console.log(data_game)
            })
            .catch(err => {
                "Error mounting data"
            })


    }

    handleCellChange = (row, col, value) => {
        const updatedDetails = [...this.state.details];

        updatedDetails[0][`col${col+1}`] = updatedDetails[0][`col${col+1}`]
            .split(',')
            .map((cell, index) => (index === row ? value : cell))
            .join(',');

        axios.post('http://localhost:8000/board/', updatedDetails[0])
            .then(r => console.log(r))
            .catch(err => console.log(err))

        this.setState({
            details: updatedDetails,
        });

        //this.onlyUpdateIfCorrect();
    };


    renderColumn(col, colIndex) {
        return (
            <div key={colIndex} className="sudoku-column">
                {col.split(",").map((cell, rowIndex) => (
                    <div className="sudoku-cell">
                    <SudokuCell
                        key={rowIndex}
                        value={cell}
                        onChange={(value) => this.handleCellChange(rowIndex, colIndex, value)}
                    />
                    </div>
                ))}
            </div>
        );
    }


    onlyUpdateIfCorrect() {
        let data_game;

        axios.get('http://localhost:8000/board/')
            .then(res => {
                data_game = res.data;

                this.setState({
                    details: data_game,
                })

                console.log(data_game)
            })
            .catch(err => {
                "Error mounting data"
            })
    }

    render() {
        return (
            <div className="sudoku-board">
                {this.state.details.map((elem, index) => (
                    [...Array(9)].map((_, colIndex) => this.renderColumn(elem[`col${colIndex + 1}`], colIndex))
                ))}
            </div>
        );
    }
}

export default SudokuBoard;