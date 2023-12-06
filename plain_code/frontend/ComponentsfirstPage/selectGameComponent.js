import React, {Component} from "react";
import './gameButtonComponent'
import GameButton from "./gameButtonComponent";
import LevelsButtons from "./levelButtonsComponent";
import axios from "axios";

class ButtonsMenu extends Component{
    state = {
        showLevelOptions: false,

    }
    handleButtonStartGame = () => {
        this.setState({showLevelOptions: true})
        console.log("incepere joc")
    }
    handleButtonContinueGame = () => {
        let data_game;

        console.log("continuam jocul")
        axios.get('http://localhost:8000/board/')
            .then(res => {
                data_game = res.data;

                this.setState({
                    details: data_game,
                })

                console.log(data_game)
            })
            .catch(err => {
                "Error mounting data"
            })

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