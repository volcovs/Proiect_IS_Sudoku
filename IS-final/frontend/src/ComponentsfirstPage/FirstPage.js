
import React, {useState} from "react";
import ButtonsMenu from "./selectGameComponent";
import "../StylingFolder/PageStyle.css";

import Login from "../LoginPage/Login";
import SignUpComponent from "../SignupPage/SignUpComponent";
import UserProfile from "../UserPage/UserProfile";

import NickiPic from "../UserPage/nickipic.jpg";
const FirstPage = ({ onSelectLevel, onClose }) => {
    const [showSignIn, setShowSignIn] = useState(false);
    const [showLogIn, setShowLogIn] = useState(false);
    const [showProfile, setShowProfile] = useState(false);

    const handleSignInClick = () => {
        setShowSignIn(true);
        setShowLogIn(false);
        setShowProfile(false);
    };

    const handleLogInClick = () => {
        setShowSignIn(false);
        setShowLogIn(true);
        setShowProfile(false);
    };

    const handleProfileClick = () => {
        setShowSignIn(false);
        setShowLogIn(false);
        setShowProfile(true);
    };
    const sampleUser = {
        username: 'exampleUser',
        profile_image: NickiPic,
        first_name: 'John',
        last_name: 'Doe',
        games_won: 10,
        games_started: 20,
        total_time: '5 hours',
        best_time: '1 hour',
    };
    return (
        <div>
            {showLogIn && <Login />}
            {showSignIn && <SignUpComponent />}

            <div className="first-page">
                <div className="title-container">
                    <h1 className="title-text">SUDOKU</h1>
                </div>
                <ButtonsMenu onSelectLevel={onSelectLevel} onClose={onClose}/>

                <div className="account-buttons">
                    <button className="op-button" onClick={handleSignInClick}> Sign in </button>
                    <button className="op-button" onClick={handleLogInClick}> Log in </button>
                    <button className="op-button" onClick={handleProfileClick}> my profile</button>
                </div>

            </div>

            {showProfile && <UserProfile />}
        </div>
    );
};

export default FirstPage;
