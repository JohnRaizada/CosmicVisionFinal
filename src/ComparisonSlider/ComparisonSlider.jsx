import React, { useRef, useState } from 'react';
import './ComparisonSlider.css';

const ComparisonSlider = ({ imageBefore, imageAfter }) => {
    const sliderRef = useRef();
    const [isDragging, setIsDragging] = useState(false);

    const handleMouseDown = () => {
        setIsDragging(true);
    };

    const handleMouseUp = () => {
        setIsDragging(false);
    };

    const handleMouseMove = (event) => {
        if (!isDragging) return;
        const x = event.pageX - sliderRef.current.offsetLeft;
        const width = window.getComputedStyle(sliderRef.current).getPropertyValue('width');
        const percent = (x / parseInt(width)) * 100;
        if (percent < 100 && percent > 0) {
            sliderRef.current.style.setProperty('--percentage', `${percent}%`);
        }
    };

    return (
        <div className="comparison-slider"
            ref={sliderRef}
            onMouseMove={handleMouseMove}
            onMouseDown={handleMouseDown}
            onMouseUp={handleMouseUp}
            onMouseLeave={handleMouseUp}>
            <img src={imageBefore} alt="Before" className="image-before non-selectable" />
            <img src={imageAfter} alt="After" className="image-after non-selectable" />
            <div className="slider">
                <span className="slider-thumb">
                    <div className="slider-dot"/>
                </span>
            </div>
        </div>
    );
};

export default ComparisonSlider;
