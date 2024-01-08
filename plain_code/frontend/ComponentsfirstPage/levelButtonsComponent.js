import React from "react";
import "../StylingFolder/ButtonStyling.css"
const LevelsButtons = ({onSelectLevel, onClose}) =>{
    const levels = ['Easy', 'Medium', 'Hard'];
    return (
        <div className="levels-buttons">
            {levels.map((level,index)=>(
                <button className="level-button" key={index} onClick={()=>onSelectLevel(2, level)}>
                    {level}
                </button>
                ))}
        </div>
    )
}
export default LevelsButtons