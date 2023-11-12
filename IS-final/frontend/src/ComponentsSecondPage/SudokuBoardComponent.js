// SudokuBoard.js
import React, { Component } from "react";
import SudokuCell from "./SudokuCellComponent";
import axios from "axios";
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0];

class SudokuBoard extends Component {
    state = {details: [], }

    constructor(props) {
        super(props);

        let data_game;

        axios.get('http://localhost:8000')
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

        updatedDetails[0][`row${row}`] = updatedDetails[0][`row${row}`]
            .split(',')
            .map((cell, index) => (index === col ? value : cell))
            .join(',');

        axios.post('http://localhost:8000', updatedDetails[0])
            .then(r => console.log(r))
            .catch(err => console.log(err))

        this.setState({
            details: updatedDetails,
        });

    };


    render() {
        return (
            <div className="sudoku-board">
                {this.state.details.map((elem, index) => (
                    <div key={index} className="sudoku-elem">
                        <div key={1} className={"sudoku-row"}>
                            {elem.row1.split(",").map((cell, colIndex) =>
                                <SudokuCell
                                    key={colIndex}
                                    value={cell}
                                    onChange={(value) =>
                                        this.handleCellChange(1, colIndex, value)
                                    }
                                />
                            )}
                        </div>

                        <div key={2} className={"sudoku-row"}>
                            {elem.row2.split(",").map((cell, colIndex) =>
                                <SudokuCell
                                    key={colIndex}
                                    value={cell}
                                    onChange={(value) =>
                                        this.handleCellChange(2, colIndex, value)
                                    }
                                />
                            )}
                        </div>

                        <div key={3} className={"sudoku-row"}>
                            {elem.row3.split(",").map((cell, colIndex) =>
                                <SudokuCell
                                    key={colIndex}
                                    value={cell}
                                    onChange={(value) =>
                                        this.handleCellChange(3, colIndex, value)
                                    }
                                />
                            )}
                        </div>

                        <div key={4} className={"sudoku-row"}>
                            {elem.row4.split(",").map((cell, colIndex) =>
                                    <SudokuCell
                                        key={colIndex}
                                        value={cell}
                                        onChange={(value) =>
                                            this.handleCellChange(4, colIndex, value)
                                        }
                                    />
                                )}
                        </div>

                        <div key={5} className={"sudoku-row"}>
                            {elem.row5.split(",").map((cell, colIndex) =>
                                    <SudokuCell
                                        key={colIndex}
                                        value={cell}
                                        onChange={(value) =>
                                            this.handleCellChange(5, colIndex, value)
                                        }
                                    />
                                )}
                        </div>

                        <div key={6} className={"sudoku-row"}>
                            {elem.row6.split(",").map((cell, colIndex) =>
                                    <SudokuCell
                                        key={colIndex}
                                        value={cell}
                                        onChange={(value) =>
                                            this.handleCellChange(6, colIndex, value)
                                        }
                                    />
                                )}
                        </div>

                        <div key={7} className={"sudoku-row"}>
                                {elem.row7.split(",").map((cell, colIndex) =>
                                        <SudokuCell
                                            key={colIndex}
                                            value={cell}
                                            onChange={(value) =>
                                                this.handleCellChange(7, colIndex, value)
                                            }
                                        />
                                    )}
                        </div>

                        <div key={8} className={"sudoku-row"}>
                                {elem.row8.split(",").map((cell, colIndex) =>
                                        <SudokuCell
                                            key={colIndex}
                                            value={cell}
                                            onChange={(value) =>
                                                this.handleCellChange(8, colIndex, value)
                                            }
                                        />
                                    )}
                        </div>

                        <div key={9} className={"sudoku-row"}>
                                {elem.row9.split(",").map((cell, colIndex) =>
                                        <SudokuCell
                                            key={colIndex}
                                            value={cell}
                                            onChange={(value) =>
                                                this.handleCellChange(9, colIndex, value)
                                            }
                                        />
                                    )}
                        </div>
                    </div>
                ))}
            </div>
        );
    }
}

export default SudokuBoard;