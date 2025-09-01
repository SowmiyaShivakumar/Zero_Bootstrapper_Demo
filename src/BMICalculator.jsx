import React, { useState } from 'react';

const BMICalculator = () => {
    const [weight, setWeight] = useState('');
    const [height, setHeight] = useState('');
    const [bmi, setBmi] = useState(null);

    const calculateBMI = (e) => {
        e.preventDefault();
        const bmiValue = weight / (height * height);
        setBmi(bmiValue);
    };

    return (
        <form onSubmit={calculateBMI}>
            <input type="number" placeholder="Weight (kg)" value={weight} onChange={(e) => setWeight(e.target.value)} />
            <input type="number" placeholder="Height (m)" value={height} onChange={(e) => setHeight(e.target.value)} />
            <button type="submit">Calculate BMI</button>
            {bmi && <p>Your BMI is: {bmi}</p>}
        </form>
    );
};

export default BMICalculator;