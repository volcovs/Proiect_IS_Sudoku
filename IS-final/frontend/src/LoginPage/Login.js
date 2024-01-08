// Login.js
import React, { useState } from 'react';
import './LoginStyling.css';
import axios from 'axios';

const LoginComponent = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        const credentials = {
            type: 'login',
            username: formData.username,
            password: formData.password,
            first_name:'d',
            last_name:'d',
            games_won: 0,
            games_total: 0,
            time_total: '00:00:00',
            best_time: '00:00:00',
        };

        try {
            const response = await axios.post('http://localhost:8000/user/', credentials);
            // Handle success if needed
            console.log('Login successful:', response.data);
        } catch (error) {
            // Handle error
            console.error('Error during login:', error);
        }
    };

    return (
        <div className="login-container">
            <form className="login-form" onSubmit={handleLogin}>
                <h1 className="login-header">Login</h1>
                <div className="login-field">
                    <label>Username:</label>
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                    />
                </div>
                <div className="login-field">
                    <label>Password:</label>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default LoginComponent;
