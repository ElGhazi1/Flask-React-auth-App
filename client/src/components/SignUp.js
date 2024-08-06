import React, { useState } from 'react';

const SignUp = () => {
  const [email, setEmail] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const response = await fetch('/api/sign-up', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        password1,
        password2,
      }),
    });

    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <div className="container mt-5">
      <h1 className="display-4">Sign Up Page</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email:</label>
          <input 
            type="email" 
            className="form-control" 
            id="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password1" className="form-label">Password:</label>
          <input 
            type="password" 
            className="form-control" 
            id="password1" 
            value={password1} 
            onChange={(e) => setPassword1(e.target.value)} 
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password2" className="form-label">Confirm Password:</label>
          <input 
            type="password" 
            className="form-control" 
            id="password2" 
            value={password2} 
            onChange={(e) => setPassword2(e.target.value)} 
          />
        </div>
        <button type="submit" className="btn btn-primary">Sign Up</button>
      </form>
      {message && <div className="mt-3">{message}</div>}
    </div>
  );
};

export default SignUp;
