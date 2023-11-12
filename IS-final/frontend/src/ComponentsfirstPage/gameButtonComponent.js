import React, {Component} from "react";

class GameButton extends Component{
    render(){
        return (<div>
            <button onClick = {this.props.onClick}>
                {this.props.text}
            </button>
            </div>
        );
    }
}
export default GameButton