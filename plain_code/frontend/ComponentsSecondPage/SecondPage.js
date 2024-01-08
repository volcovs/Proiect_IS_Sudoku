import React, { Component } from "react";
import axios from "axios";
import "./SudokuBoardComponent";
import "../StylingFolder/PageStyle.css";
import SudokuBoard from "./SudokuBoardComponent";
import Timer from "./Timer";

class SecondPage extends Component {
    constructor(props) {
        super(props);
        this.sudokuBoardRef = React.createRef();
    }
    state = {
        text: "",
        timerPaused: false,
        hintCounter: 0,
        hint: 0,
        xhint: 0,
        yhint: 0,
    };

    componentDidMount() {
        this.fetchErrorMessage();

    }

    fetchErrorMessage() {
        axios
            .get("http://localhost:8000/errmsgs/")
            .then((res) => {
                const msg = res.data;
                this.setState({
                    text: msg[0]?.msg || "",
                });
                console.log(this.state.text);
            })
            .catch((err) => {
                console.error("Error fetching error message:", err);
            });
    }

    handleTimerStop = () => {
        this.setState({
            timerPaused: true,
        });
    };

    handleTimerStart = () => {
        this.setState({
            timerPaused: false,
        });
    };

    handleVictory = () => {
        this.setState({
            timerPaused: true,
        })

        //send timer information to Django, for statistics
    }
    handleHint = () => {
        const { hintCounter } = this.state;

        if (hintCounter < 3) {

            axios
                .get('http://localhost:8000/hint/')
                .then((res) => {
                    console.log('Complete response from server:', res);
                    const { hint, xhint, yhint } = res.data[0];
                    console.log('Received hints:', hint, xhint, yhint);

                    // Update the state to store the received hints
                    this.setState({
                        hint: hint,
                        xhint: xhint,
                        yhint: yhint,
                    });

                    this.sudokuBoardRef.current.handleHints(hint, xhint, yhint);

                    // Perform actions to show the hints to the user
                    // You can customize this part based on how you want to display hints
                    console.log(`Hint: ${hint}, X Hint: ${xhint}, Y Hint: ${yhint}`);
                })
                .catch((err) => {
                    // Handle error
                    console.error('Error fetching hint:', err);
                });
            this.setState((prevState) => ({
                hintCounter: prevState.hintCounter + 1,
            }));

            // Perform any other actions related to showing the hint
        } else {
            // Hint limit reached, button should be disabled
            console.log("Hint limit reached. Button disabled.");
        }
    };

    render() {
        this.fetchErrorMessage(); // Fetch the error message dynamically

        return (
            <div>
                <div className="title-container">
                    <h1 className="title-text">SUDOKU</h1>
                </div>
                <Timer onPause={this.handleTimerStop} onStart={this.handleTimerStart} timerPause={this.state.timerPaused} />
                <SudokuBoard
                    timerPaused={this.state.timerPaused}
                    onVictory={this.handleVictory}
                    ref={this.sudokuBoardRef}
                    hint={this.state.hint}
                    xhint={this.state.xhint}
                    yhint={this.state.yhint}
                />
                <h3 className="text-message">{this.state.text}</h3>
                <button
                    className="game-button"
                    onClick={this.handleHint}
                    disabled={this.state.hintCounter >= 3}
                >
                    Hint
                </button>
                <div className="hint-counter">
                    Hints Left: {3 - this.state.hintCounter}
                </div>
            </div>
        )
    }
}

export default SecondPage;
