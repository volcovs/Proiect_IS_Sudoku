// SudokuCell.js
import React, { Component } from "react";
import axios from 'axios';

class SudokuCell extends Component {
    handleChange = (e) => {
        const inputValue = e.target.value;
        // You can add validation or formatting logic here if needed
        this.props.onChange(inputValue);

        //axios.post('http://localhost:8000');
            //send modifications to the server
        //);
    };

    render() {
        return (
            <input
                type="number"
                min="0"
                max="9"
                value={this.props.value}
                onChange={this.handleChange}
            />
        );
    }
}

export default SudokuCell;