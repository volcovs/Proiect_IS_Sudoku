import React, { useState, useEffect } from 'react';

const Timer = () => {
    const [seconds, setSeconds] = useState(0); // Initial value for the timer

    useEffect(() => {
        const timer = setInterval(() => {
            // Increase the seconds by 1
            setSeconds(prevSeconds => prevSeconds + 1);
        }, 1000);

        // Clean up the timer when the component unmounts
        return () => clearInterval(timer);
    }, []); // The empty dependency array ensures that the effect runs only once

    // Convert seconds to minutes and seconds for display
    const displayTime = () => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    };

    return (
        <div>
            <p>{displayTime()}</p>
        </div>
    );
};

export default Timer;
