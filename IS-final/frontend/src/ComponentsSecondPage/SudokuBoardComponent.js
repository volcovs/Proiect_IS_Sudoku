import React, { Component } from "react";
import SudokuCell from "./SudokuCellComponent";
import axios from "axios";
import "../StylingFolder/SudokuBoardStyle.css";

class SudokuBoard extends Component {
    state = {
        details: [],
        originalBoard: [],
        fetched: false,
        victoryMsg: false,
        clickedCell: { row: 5, col: 5 },
        hint: 0,
        xhint: 0,
        yhint: 0,
    };
    handleCellClick = (row, col) => {

        this.setState({
            clickedCell: {row:row, col:col},
        });

    };
    componentDidMount() {
        this.fetchBoardData();
        this.fetchVictoryMsg();
    }

    fetchBoardData() {
        axios
            .get("http://localhost:8000/board/")
            .then((res) => {
                const data_game = res.data;
                this.setState({
                    details: data_game,
                    originalBoard: data_game,
                    fetched: true,
                });
                console.log(data_game);
            })
            .catch((err) => {
                console.error("Error fetching board data:", err);
            });
    }

    fetchVictoryMsg() {
        const { onVictory } = this.props;

        axios
            .get("http://localhost:8000/victorymsgs/")
            .then((res) => {
                const msg = res.data;
                const text = msg[0]?.msg || "False";
                this.setState({
                    victoryMsg: text !== "False",
                });

                if (this.state.victoryMsg === true) {
                    // Display alert when victory condition is met
                    window.alert("YOU WON! Go back to start a new game");
                    onVictory();
                }
            })
            .catch((err) => {
                console.error("Error fetching victory message:", err);
            });
    }

    handleCellChange = (row, col, value) => {
        const { timerPaused } = this.props;

        if (!timerPaused) {
            const updatedDetails = [...this.state.details];
            const original = JSON.parse(JSON.stringify(this.state.originalBoard));

            if (original[0][`col${col + 1}`].split(",")[row] === "0") {
                updatedDetails[0][`col${col + 1}`] = updatedDetails[0][`col${col + 1}`]
                    .split(",")
                    .map((cell, index) => (index === row ? value : cell))
                    .join(",");

                axios
                    .post("http://localhost:8000/board/", updatedDetails[0])
                    .then((r) => console.log(r))
                    .catch((err) => console.error("Error posting board data:", err));

                this.setState({
                    details: updatedDetails,
                    originalBoard: original,
                    fetched: true,
                });

            }
        }
    };

    handleHints = (hint, xhint, yhint) => {

        const { details } = this.state;

        // Create a deep copy of the details array
        console.log(details);
        const updatedDetails = JSON.parse(JSON.stringify(details));
        console.log(updatedDetails);
        // Update the value of the hinted cell
        updatedDetails[0][`col${xhint + 1}`] = updatedDetails[0][`col${xhint + 1}`]
            .split(",")
            .map((cell, index) => (index === yhint? hint : cell))
            .join(",");

        this.setState({
            details: updatedDetails,
            hint: hint,
            xhint: xhint,
            yhint: yhint,
        });
    };

    renderColumn(col, colIndex) {
        const {clickedCell} = this.state;
        return (
            <div key={colIndex} className="sudoku-column">
                {col.split(",").map((cell, rowIndex) => (
                    <div key={rowIndex}
                         className={`sudoku-cell ${
                             clickedCell &&
                             (rowIndex === clickedCell.row || colIndex === clickedCell.col)
                                 ? "almostclicked-cell"
                                 : ""
                         }`}
                         onClick={() => this.handleCellClick(rowIndex, colIndex)}
                    >
                        <SudokuCell
                            value={cell}
                            onChange={(value) =>
                                this.handleCellChange(rowIndex, colIndex, value)
                            }

                        />
                    </div>

                ))}
            </div>
        );
    }

    render() {
            const { details } = this.state;

            return (
                <div className="sudoku-board">
                    {details.map((elem, index) =>
                        [...Array(9)].map((_, colIndex) =>
                            this.renderColumn(elem[`col${colIndex + 1}`], colIndex)
                        )
                    )}
                </div>
            );
    }
}

export default SudokuBoard;
