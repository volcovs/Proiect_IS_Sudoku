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
        console.log("continuam jocul")
    }
    render(){
       return (
           <div>
               <GameButton onClick = {this.handleButtonContinueGame} text = "continue  game"/>
               <GameButton onClick = {this.handleButtonStartGame} text = "start new game"/>

               {this.state.showLevelOptions &&
               <LevelsButtons/>}
           </div>
       )
    }

}
export default ButtonsMenu