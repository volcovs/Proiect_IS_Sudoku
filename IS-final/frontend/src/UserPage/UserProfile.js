// UserProfile.js
import React, {Component} from 'react';
import "./UserProfileStyling.css"
import profile_pic from "./profile_pic.jpg"
import axios from "axios";
class UserProfile extends Component {
    state = {
        type: "get",
        username: '',
        password: '',
        first_name: '',
        last_name: '',
        games_won: 0,
        games_total: 0,
        time_total: '',
        best_time: '',
    };
    componentDidMount() {
        this.fetchUserData();
    }
    fetchUserData() {
        axios
            .get("http://localhost:8000/user/")
            .then((res) => {
                const user = res.data[0];
                this.setState({ ...user });
            })
            .catch((err) => {
                console.error("Error fetching user data:", err);
            });
    }
    render()
    {
        const {
            type,
            username,
            password,
            first_name,
            last_name,
            games_won,
            games_total,
            time_total,
            best_time,
        } = this.state;

        return (
            <div className="user-profile-container">
                <div className="user-profile-form">
                    <h1 className="user-profile-header">User Profile</h1>
                    <div className="user-profile-field">
                        <label>Profile Image:</label>
                        <img src={profile_pic} alt="Profile" className="profile-image"/>
                    </div>
                    <div className="user-profile-field">
                        <label>Username:</label>
                        <input type="text" value={username} readOnly/>
                    </div>

                    <div className="user-profile-field">
                        <label>First Name:</label>
                        <input type="text" value={first_name} readOnly/>
                    </div>

                    <div className="user-profile-field">
                        <label>Games Won:</label>
                        <input type="text" value={games_won} readOnly/>
                    </div>
                    <div className="user-profile-field">
                        <label>Games Started:</label>
                        <input type="text" value={games_total} readOnly/>
                    </div>
                </div>
            </div>
        );
    }
};

export default UserProfile;
