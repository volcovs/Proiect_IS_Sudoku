import React from "react";
import "../StylingFolder/ButtonStyling.css"
const LevelsButtons = ({onSelectLevel, onClose}) =>{
    const levels = ['Easy', 'Medium', 'Hard'];
    return (
        < div className="levels-buttons">
            {levels.map((level,index)=>(
                <button className="game-button" key={index} onClick={()=>onSelectLevel({level})}>
                    {level}
                </button>
                ))}
        </div>
    )
}
export default LevelsButtons