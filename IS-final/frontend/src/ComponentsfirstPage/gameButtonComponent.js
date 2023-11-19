import React, {Component} from "react";
import "../StylingFolder/ButtonStyling.css"
class GameButton extends Component{
    render(){
        return (<div>
            <button className="game-button" onClick = {this.props.onClick}>
                {this.props.text}
            </button>
            </div>
        );
    }
}
export default GameButton