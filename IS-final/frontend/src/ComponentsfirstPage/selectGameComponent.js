import React, {Component} from "react";
import './gameButtonComponent'
import GameButton from "./gameButtonComponent";
import LevelsButtons from "./levelButtonsComponent";

class ButtonsMenu extends Component{
    state = {
        showLevelOptions: false,

    }
    handleButtonStartGame = () => {
        this.setState({showLevelOptions: true})
        console.log("incepere joc")
    }
    handleButtonContinueGame = () => {
        const { onSelectLevel, onClose } = this.props;
        onSelectLevel(2, "Continue");
        console.log("continuam jocul")

    }
    render(){
        const { onSelectLevel, onClose } = this.props;

       return (
           <div>

               <GameButton onClick = {this.handleButtonContinueGame} text = "continue  game"/>

               {(! this.state.showLevelOptions) &&
               <GameButton onClick = {this.handleButtonStartGame} text = "start new game"/>}

               {this.state.showLevelOptions &&
               <LevelsButtons onSelectLevel={onSelectLevel} onClose={onClose}/>}

           </div>
       )
    }

}
export default ButtonsMenu