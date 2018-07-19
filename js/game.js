(function(){
    "use strict";
    let field = document.getElementsByClassName("gamefield")[0];

    let NR_ROWS = 20;
    let NR_COLS = 20;
    let ALIVE_V = 1;
    let DEAD_V  = 0;

    /*
    * Start function for game
     */
    function start(){
        let gamefield = init_game();
        console.log(gamefield);
    }



    /*
    * Create random integer
     */
    function randomInt (low, high) {
        return Math.floor(Math.random() * (high - low + 1) + low);
    }



    /*
    * Create a 2d array as gamefiled
     */
    function init_game(){
        let gamefield = new Array(NR_ROWS);
        for (let i = 0; i < NR_ROWS; i++) {
            gamefield[i] = Array.from({length: NR_COLS}, () => randomInt(0, 1));
        }
        return gamefield;
    }


    start();
})()