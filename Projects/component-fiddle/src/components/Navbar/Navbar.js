import React from 'react';
import './Navbar.css'

function Navbar(props) {
    return (
        <div className="Navbar">
            {props.firstbar + ' '}
            {props.secondbar + ' '}
            {props.thirdbar + ' '}
            {props.fourthbar + ' '}
            {props.fifthbar + ' '}
        </div>
    );
}

export default Navbar