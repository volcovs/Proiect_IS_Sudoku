import React from "react";
import "./SudokuBoardComponent";
import "../StylingFolder/TitleStyling.css";
import ButtonsMenu from "../ComponentsfirstPage/selectGameComponent";
import SudokuBoard from "./SudokuBoardComponent";
const SecondPage = () => {
    return (
        <div className="second-page">
            <div className="title-container">
                <h1 className="title-text">SUDOKU</h1>
            </div>
            <SudokuBoard />
        </div>
    );

};
export default SecondPage