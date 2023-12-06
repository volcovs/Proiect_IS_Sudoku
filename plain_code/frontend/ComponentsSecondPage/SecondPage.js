import React, {Component} from "react";
import "./SudokuBoardComponent";
import "../StylingFolder/TitleStyling.css";
import ButtonsMenu from "../ComponentsfirstPage/selectGameComponent";
import SudokuBoard from "./SudokuBoardComponent";
import axios from "axios";
import {render} from "@testing-library/react";

class SecondPage extends Component {
    state = {text: "", }

    constructor(props) {

        super(props);
        let msg;

        axios.get('http://localhost:8000/errmsgs/')
            .then(res => {
                msg = res.data;

                this.setState({
                    text: msg[0][`msg`],
                })

                console.log(this.state.text);
            })
            .catch(err => {
                "Error mounting data"
            })
    }

    getMessage() {
        let msg;

        axios.get('http://localhost:8000/errmsgs/')
            .then(res => {
                msg = res.data;

                this.setState({
                    text: msg[0][`msg`],
                })
            })
            .catch(err => {
                "Error mounting data"
            })

        return this.text;
    }

        render()
        {
            this.getMessage();

            return (
                <div className="second-page">
                    <div className="title-container">
                        <h1 className="title-text">SUDOKU</h1>
                    </div>
                    <SudokuBoard/>
                    <h3 className="text-message">{this.state.text}</h3>
                </div>
            );
        }

};
export default SecondPage