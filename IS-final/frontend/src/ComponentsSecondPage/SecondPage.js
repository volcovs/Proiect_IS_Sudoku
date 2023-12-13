import React, { Component } from "react";
import axios from "axios";
import "./SudokuBoardComponent";
import "../StylingFolder/TitleStyling.css";
import SudokuBoard from "./SudokuBoardComponent";
import Timer from "./Timer";

class SecondPage extends Component {
    state = {
        text: "",
        timerPaused: false,
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

    render() {
        this.fetchErrorMessage(); // Fetch the error message dynamically

        return (
            <div className="second-page">
                <div className="title-container">
                    <h1 className="title-text">SUDOKU</h1>
                </div>
                <Timer onPause={this.handleTimerStop} onStart={this.handleTimerStart} timerPause={this.state.timerPaused} />
                <SudokuBoard timerPaused={this.state.timerPaused} onVictory={this.handleVictory} />
                <h3 className="text-message">{this.state.text}</h3>
                <button className="game-button">Hint</button>
            </div>
        );
    }
}

export default SecondPage;
