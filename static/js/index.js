const angleRange = document.getElementById('angle-control');
const angleResult = document.getElementById('angle-result');
const root = document.querySelector('HTML');
const boxes = document.querySelectorAll('.box');

angleRange.addEventListener("input", function() {
    const angle = angleRange.value;
    const angleRad = angle * Math.PI / 180;
    const magicNumber = Math.abs(Math.tan(angleRad) / 2);
    angleResult.innerHTML = angleRange.value + " deg";
    document.documentElement.style.setProperty('--angle', angleRange.value + 'deg');
    document.documentElement.style.setProperty('--magic-number', magicNumber);

    // Sadly the animation only updates correctly in Firefox :-(
    boxes.forEach((box) => {
        box.style.animation = "none";
    });
}, false);