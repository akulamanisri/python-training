import React, { useState } from 'react';

const CricketScore = (props) => {
    console.log("props", props);
    console.log("target =", props.target);

    const [runs, setRuns] = useState(0);
    const [wickets, setWickets] = useState(0);
    const [target, setTarget] = useState(props.target);

    // 🆕 Track total balls bowled
    const [ballsBowled, setBallsBowled] = useState(0);

    // Constants
    const totalOvers = 20; // Or receive from props
    const ballsPerOver = 6;
    const totalBalls = totalOvers * ballsPerOver;

    // 🧮 Derived values
    const oversCompleted = Math.floor(ballsBowled / ballsPerOver);
    const ballsInCurrentOver = ballsBowled % ballsPerOver;
    const oversLeft = totalOvers - oversCompleted - (ballsInCurrentOver > 0 ? 1 : 0);

    // 🏏 Handle run
    const handleRuns = (run) => {
        if (runs + run >= target) {
            alert("Target Chased");
        }

        if (ballsBowled < totalBalls && wickets < 10 && runs < target) {
            setRuns(runs + run);
            setBallsBowled(ballsBowled + 1);
        }
    };

    // 🧷 Handle wicket
    const handleWicket = () => {
        if (wickets + 1 === 10) {
            alert("All Out");
        }

        if (ballsBowled < totalBalls && wickets < 10 && runs < target) {
            setWickets(wickets + 1);
            setBallsBowled(ballsBowled + 1);
        }
    };

    return (
        <>
            <h1>Score: {runs} / {wickets}</h1>
            <h2>Current Over: {oversCompleted}.{ballsInCurrentOver}</h2>
            <h2>Overs Left: {oversLeft}</h2>

            {
                (wickets < 10 && runs < target && ballsBowled < totalBalls) ? (
                    <div>
                        <button onClick={() => handleRuns(6)}>Six</button>
                        <button onClick={() => handleRuns(4)}>Four</button>
                        <button onClick={() => handleRuns(3)}>Three</button>
                        <button onClick={() => handleRuns(2)}>Two</button>
                        <button onClick={() => handleRuns(1)}>One</button>
                        <button onClick={() => handleRuns(0)}>Dot Ball</button>
                        <button onClick={handleWicket}>Wicket</button>
                    </div>
                ) : (
                    <h2>Game Over</h2>
                )
            }
        </>
    );
};

export default CricketScore;

