
import React from "react";
import ButtonsMenu from "./selectGameComponent";
import "../StylingFolder/TitleStyling.css"; // Import the CSS file

const FirstPage = ({ onSelectLevel, onClose }) => {
    return (
        <div className="first-page">
            <div className="title-container">
                <h1 className="title-text">SUDOKU</h1>
            </div>
            <ButtonsMenu onSelectLevel={onSelectLevel} onClose={onClose}/>
        </div>
    );
};

export default FirstPage;
