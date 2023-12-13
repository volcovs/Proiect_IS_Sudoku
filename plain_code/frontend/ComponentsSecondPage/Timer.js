import React, { useState, useEffect } from 'react';

const Timer = ({onPause, onStart, timerPause}) => {
    const [seconds, setSeconds] = useState(0); // Initial value for the timer
    const [isPaused, setIsPaused] = useState(false); // New state for tracking whether the timer is paused

    useEffect(() => {
        const timer = setInterval(() => {
            if (!isPaused) {
                // Increase the seconds by 1 only if the timer is not paused
                setSeconds((prevSeconds) => prevSeconds + 1);
            }
        }, 1000);

        // Clean up the timer when the component unmounts
        return () => clearInterval(timer);
    }, [isPaused]); // Include isPaused in the dependency array to update the effect when isPaused changes

    // Convert seconds to minutes and seconds for display
    const displayTime = () => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    };

    // Function to handle the button click and toggle the paused state
    const handlePauseClick = () => {
            setIsPaused((prevIsPaused) => !prevIsPaused);
            if (isPaused) {
                onStart();
            }
            else {
                onPause();
            }
    };

    const verifyCurrentState = () => {
        if (timerPause === true) {
            setIsPaused((prevIsPaused) => !prevIsPaused);
            if (isPaused) {
                onStart();
            }
            else {
                onPause();
            }
        }
    }

    return (
        <div className="timer-container">
            <p>{displayTime()}</p>
            <button className="game-button" onClick={handlePauseClick}>
                {isPaused ? 'Resume' : 'Pause'}
            </button>
        </div>
    );
};

export default Timer;
