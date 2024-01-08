// SignUp.js
import React, { useState } from 'react';
import './SignupStyling.css';
import axios from 'axios';
const SignUpComponent = () => {
    const [formData, setFormData] = useState({
        username: '',
        firstName: '',
        lastName: '',
        password: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newUser = {
            type: 'create', // Assuming 'create' is the type for signup
            username: formData.username,
            password: formData.password,
            first_name: formData.firstName,
            last_name: formData.lastName,
            games_won: 0,
            games_total: 0,
            time_total: '00:00:00',
            best_time: '00:00:00',
            };

            axios
                .post('http://localhost:8000/user/', newUser)
                .then((res) => {
                    // Handle success if needed
                    console.log('Signup successful:', res.data);
                })
                .catch((err) => {
                    // Handle error
                    console.error('Error during signup:', err);});
    };

    return (
        <div className="signup-container">
            <form className="signup-form" onSubmit={handleSubmit}>
                <h1 className="signup-header">Sign Up</h1>
                <div className="signup-field">
                    <label> Username: </label>
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                    />
                </div>
                <div className="signup-field">
                <label> First Name: </label>
                    <input
                        type="text"
                        name="firstName"
                        value={formData.firstName}
                        onChange={handleChange}
                    />
                </div>
                <div className="signup-field">
                    <label> Last Name: </label>
                    <input
                        type="text"
                        name="lastName"
                        value={formData.lastName}
                        onChange={handleChange}
                    />
                </div>
                <div className="signup-field">
                    <label> Password: </label>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                    />
                </div>

                <button type="submit">Sign Up</button>
            </form>
        </div>
    );
};

export default SignUpComponent;
