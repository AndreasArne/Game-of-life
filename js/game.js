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

        document.querySelector("canvas").onclick= function() {
            window.requestAnimationFrame(game_loop);
        };
        // window.requestAnimationFrame(game_loop);

        // game_loop();
    }



    /*
    * Infinity loop the game
     */
    async function game_loop() {
        // while(true) {
        //

        await sleep(3000);
            console.log("HEJ");
            BUFFER.clearRect(0, 0, BUFFER.canvas.width, BUFFER.canvas.height);
            CONTEXT.clearRect(0, 0, CONTEXT.canvas.width, CONTEXT.canvas.height);
            BUFFER.beginPath();
            CONTEXT.beginPath();
            BUFFER.closePath();
            CONTEXT.closePath();
            tick();
            draw_gamefield();
            BUFFER.fill();
            CONTEXT.fill();
            // resize();
            console.log("OMPALOMP");
        // }
    }



    /*
    * Calculates a tick.
    * During a tick, each cell is check against the rules.
    */
    function tick() {
        let tick_changes = [];
        for(let row=0; row<NR_ROWS; row++) {
            for(let col=0; col<NR_ROWS; col++) {
                let neighbor_value = get_neighborhood(row, col);
                let rule = check_rules(GAMEFIELD[row, col], neighbor_value);
                if (rule > 0) {
                    tick_changes.push((row, col, rule));
                }
            }
        }
        activate_rules(tick_changes);
    }



    /*
    * Activate rules for each changed cell on gamefield
     */
    function activate_rules(tick) {
        let row_i = 0, col_i = 1, rule_i = 2;
        tick.forEach(function(change) {
            let rule = change[rule_i];
            let row = change[row_i];
            let col = change[col_i];

            if (rule == 1) {
                // Any live cell with fewer than two live neighbors dies, as if by under population.
                GAMEFIELD[row][col] = DEAD_V;
            }
            else if (rule == 3) {
                // Any live cell with more than three live neighbors dies, as if by overpopulation.
                GAMEFIELD[row][col] = DEAD_V
            }
            else if (rule == 4) {
                // Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                GAMEFIELD[row][col] = ALIVE_V
            }
        });
    }



    /*
    * Check rule for cell
     */
    function check_rules(alive, n_value) {
        if (alive && n_value < 2) { // 1
            // Any live cell with fewer than two live neighbors dies, as if by under population.
            return 1;
        } else if (alive && 1 < n_value && n_value < 4) { // 2-3
            // Any live cell with two or three live neighbors lives on to the next generation.
            return -1;
        } else if (alive && n_value > 3) { // > 3
            // Any live cell with more than three live neighbors dies, as if by overpopulation.
            return 3;
        } else if ( !alive && n_value == 3) { // 3
            // Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            return 4;
        } else {
            return -1
        }
    }



    /*
    * Calculate neighborhood value for a cell
    */
    function get_neighborhood(row, col) {
        let last_rowI = NR_ROWS - 1;
        let last_colI = NR_COLS - 1;

        let above_ind = row == 0 ? last_rowI : row - 1;
        let below_ind = row == last_rowI ? 0 : row + 1;
        let left_ind = col == 0 ? last_colI : col - 1;
        let right_ind = col == last_colI ? 0 : col + 1;

        let above = 0, below = 0, left = 0,  right = 0;

        if (col == 0) {
            above = GAMEFIELD[above_ind].slice(col, col+2).reduce((a, b) => a + b) + GAMEFIELD[above_ind][left_ind];
            below = GAMEFIELD[below_ind].slice(col, col+2).reduce((a, b) => a + b) + GAMEFIELD[below_ind][left_ind];
        } else if (col == last_colI){
            above = GAMEFIELD[above_ind].slice(col-1, col+1).reduce((a, b) => a + b) + GAMEFIELD[above_ind][right_ind];
            below = GAMEFIELD[below_ind].slice(col-1, col+1).reduce((a, b) => a + b) + GAMEFIELD[below_ind][right_ind];
        } else {
            above = GAMEFIELD[above_ind].slice(col-1, col+2).reduce((a, b) => a + b);
            below = GAMEFIELD[below_ind].slice(col-1, col+2).reduce((a, b) => a + b);
        }
        left  = GAMEFIELD[row][left_ind];
        right  = GAMEFIELD[row][right_ind];

        let neighbor_sum = above + below + left + right;
        return neighbor_sum;
    }



    /*
    * Check if range for column index will be out-of-bounds.
    * Only applicable for over size not below size, -1.
    */
    function last_column(index) {
        return index == NR_COLS-1;
    }



    /*
    * calculate if row or column is out of bounds.
    */
    function calc_out_of_bounds(index, type_of) {
        return type_of == "r" ? index % NR_ROWS : index % NR_COLS;
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
      window.requestAnimationFrame(game_loop);

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



    /*
    * Simple sleep function
     */
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }



    window.addEventListener("resize", resize, {passive:true});
    start();
})()