// SudokuBoard.js
import React, { Component } from "react";
import SudokuCell from "./SudokuCellComponent";

class SudokuBoard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            board: [
                [5, 3, "", "", 7, "", "", "", ""],
                [6, "", "", 1, 9, 5, "", "", ""],
                ["", 9, 8, "", "", "", "", 6, ""],
                [8, "", "", "", 6, "", "", "", 3],
                [4, "", "", 8, "", 3, "", "", 1],
                [7, "", "", "", 2, "", "", "", 6],
                ["", 6, "", "", "", "", 2, 8, ""],
                ["", "", "", 4, 1, 9, "", "", 5],
                ["", "", "", "", 8, "", "", 7, 9],
            ],
        };
    }

    handleCellChange = (row, col, value) => {
        const newBoard = [...this.state.board];
        newBoard[row][col] = value;
        this.setState({ board: newBoard });
    };

    render() {
        return (
            <div className="sudoku-board">
                {this.state.board.map((row, rowIndex) => (
                    <div key={rowIndex} className="sudoku-row">
                        {row.map((cell, colIndex) => (
                            <SudokuCell
                                key={colIndex}
                                value={cell}
                                onChange={(value) =>
                                    this.handleCellChange(rowIndex, colIndex, value)
                                }
                            />
                        ))}
                    </div>
                ))}
            </div>
        );
    }
}

export default SudokuBoard;