// to catch JS mistakes early
'use strict';

window.onload = function (){
    // when the page finishes loading

    function getRandomInt() {
        // returns a random integer 1-100
        return Math.floor(Math.random()*100);
    }
    
    function updatePage() {
        // updates the page display
        document.getElementById('rand').innerHTML = getRandomInt().toString();
    }
    
    window.setInterval(updatePage, 1000); // every 1000 milliseconds = 1 second
    
};