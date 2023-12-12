// SudokuBoard.js
import React, { Component } from "react";
import SudokuCell from "./SudokuCellComponent";
import axios from "axios";
import "../StylingFolder/SudokuBoardStyle.css"

class SudokuBoard extends Component {state = {details: [], originalBoard: [], fetched: false}
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    constructor(props) {
        super(props);
        let data_game;

        if (this.state.fetched === false) {
            axios.get('http://localhost:8000/board/')
                .then(res => {
                    data_game = res.data;
                    this.setState({
                        details: data_game,
                        originalBoard: data_game,
                        fetched: true,
                    })

                    console.log(data_game)
                })
                .catch(err => {
                    "Error mounting data"
                })
        }
        else {
            axios.get('http://localhost:8000/board/')
                .then(res => {
                    data_game = res.data;
                    this.setState({
                        details: data_game,
                        originalBoard: this.state.originalBoard,
                        fetched: true,
                    })

                    console.log(data_game)
                })
                .catch(err => {
                    "Error mounting data"
                })
        }

    }

    handleCellChange = (row, col, value) => {
        const { timerPaused } = this.props;

        const updatedDetails = [...this.state.details];
        //deep copy, to avoid modifications to the original board
        const original = JSON.parse(JSON.stringify(this.state.originalBoard));

        //compare to the original board, in order to stop the modifications made during the game to
        //unmodifiable values
        if (timerPaused === false) {
            if (original[0][`col${col + 1}`].split(',')[row] === '0') {
                updatedDetails[0][`col${col + 1}`] = updatedDetails[0][`col${col + 1}`]
                    .split(',')
                    .map((cell, index) => (index === row ? value : cell))
                    .join(',');

                axios.post('http://localhost:8000/board/', updatedDetails[0])
                    .then(r => console.log(r))
                    .catch(err => console.log(err))

                //update the state, but keep the original board unmodified
                this.setState({
                    details: updatedDetails,
                    originalBoard: original,
                    fetched: true,
                });
            }
        }
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

    render() {
        let msg;
        let flag = false;

        axios.get('http://localhost:8000/victorymsgs/')
            .then(res => {
                msg = res.data;
                let text = msg[0][`msg`];

                flag = text !== "False";
            })
            .catch(err => {
                "Error mounting data"
            })


        if (flag === false) {
            return (
                <div className="sudoku-board">
                    {this.state.details.map((elem, index) => (
                        [...Array(9)].map((_, colIndex) => this.renderColumn(elem[`col${colIndex + 1}`], colIndex))
                    ))}
                </div>
            );
        }
        else {
            return (
                <div className="victory-msg">
                    <h1>YOU WON!</h1>
                </div>
            );
        }
    }
}

export default SudokuBoard;