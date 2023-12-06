// SudokuCell.js
import React, { Component } from "react";

class SudokuCell extends Component {
    handleChange = (e) => {
        const inputValue = e.target.value;
        // You can add validation or formatting logic here if needed
        this.props.onChange(inputValue);
    };

    render() {
        return (
            <input
                type="number"
                min="1"
                max="9"
                value={this.props.value === '0' ? "" : this.props.value}
                onChange={this.handleChange}
            />
        );
    }
}

export default SudokuCell;