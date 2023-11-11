import React from "react";
const LevelsButtons = () =>{
    const levels = ['Easy', 'Medium', 'Hard', 'Expert'];
    return (
        < div className="levels-buttons">
            {levels.map((level,index)=>(
                <button key={index} >
                    {level}
                </button>
                ))}
        </div>
    )
}
export default LevelsButtons