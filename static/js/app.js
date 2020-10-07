document.addEventListener('DOMContentLoaded', () => {
    let cardWidth = document.getElementById('0').width
        // document.getElementById('0').height = cardWidth;

    // console.log(blogs.length)

    let memberSelect = document.getElementById('memberSelect')

    memberSelect.onchange = function() {

        window.open(this.options[this.selectedIndex].value, '_self');
    };







})