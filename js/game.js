(function(){
    "use strict";

    let NR_ROWS = 20;
    let NR_COLS = 20;
    let GAMEFIELD = [];
    let ALIVE_V = 1;
    let DEAD_V  = 0;
    let SIZE = 32; //size of rectangles
    let BUFFER, CONTEXT;
    BUFFER = document.createElement("canvas").getContext("2d");
    CONTEXT = document.querySelector("canvas").getContext("2d");

    BUFFER.canvas.width = NR_ROWS * SIZE;
    BUFFER.canvas.height = NR_COLS * SIZE;
    /*
    * Start function for game
     */
    function start(){
        init_gamefield();
    }



    /*
    * Infinity loop the game
     */
    function game_loop() {
        while(true) {
            console.log(GAMEFIELD);
            tick();
            // add sleep
        }
    }



    /*
    * Calculates a tick.
    * During a tick, each cell is check against the rules.
     */
     function tick() {

     }



    /*
    * Create random integer
     */
    function randomInt (low, high) {
        return Math.floor(Math.random() * (high - low + 1) + low);
    }



    /*
    * Create a 2d array as gamefield
     */
    function init_gamefield(){
        GAMEFIELD = new Array(NR_ROWS);
        for (let i = 0; i < NR_ROWS; i++) {
            GAMEFIELD[i] = Array.from({length: NR_COLS}, () => randomInt(0, 1));
        }

        resize();
    }



    /*
    * Draw canvas gamefield.
    * Got code from https://github.com/frankarendpoth/frankarendpoth.github.io/blob/master/content/pop-vlog/javascript/2017/012-tile-world/tile-world.js
     */
    function draw_gamefield() {
        for (let i = 0; i < GAMEFIELD.length; i ++) {
            for (let j = 0; j < GAMEFIELD[i].length; j ++) {
                BUFFER.fillStyle = (GAMEFIELD[i][j] == 1)?"#000000":"#ffffff";
                BUFFER.fillRect(i*SIZE, j*SIZE, SIZE, SIZE);
        }
      }

      CONTEXT.drawImage(BUFFER.canvas, 0, 0, BUFFER.canvas.width, BUFFER.canvas.height, 0, 0, CONTEXT.canvas.width, CONTEXT.canvas.height);
    };



    /*
    * Resizes gamefield when window changes
     */
    function resize(event) {

        CONTEXT.canvas.width = Math.floor(document.documentElement.clientWidth - SIZE);

        if (CONTEXT.canvas.width > document.documentElement.clientHeight) {
            CONTEXT.canvas.width = Math.floor(document.documentElement.clientHeight);
        }
        CONTEXT.canvas.height = Math.floor(CONTEXT.canvas.width * 0.5625);

        draw_gamefield();
    };


    window.addEventListener("resize", resize, {passive:true});
    start();
})()