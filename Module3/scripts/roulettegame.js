const gamearea = document.querySelector('.gamearea');
const score  = createEle(gamearea,'div','Score :','score');
const btn = createEle(gamearea,'button','Spin','btn');
const message = createEle(gamearea,'div','Press Spin','message');
const output = createEle(gamearea,'div','','output');
const game = {x:7,y:9,coins:50,sel:[],eles:[],winner:false,styler:['black','white']};
const total = game.x * game.y;
btn.disabled = true; //can't play until bet is placed
btn.addEventListener('click',spinner);

createBoard();
updateScore();

function spinner(){
    btn.disabled = true;
    const ranVal = Math.floor(Math.random()*total)+1;
    console.log(ranVal);
    game.winner = ranVal-1; //winner is set and styles box to a specific color
    game.styler = [game.eles[ranVal-1].style.backgroundColor,game.eles[ranVal-1].style.color];
    const win = game.sel.includes(ranVal); //
    console.log(win);

    const eles = output.querySelectorAll('.bet');
    eles.forEach((el)=>{ //removes the previous bets from the board
        el.remove();
        console.log(el);
    })
    if(win){
        const winAmount = total;
        game.coins += winAmount; 
        message.innerHTML = `Winner on ${ranVal} you won ${winAmount}`; //prints out winner and value of winnings
        createEle(game.eles[ranVal-1],'div','$','bet');
        game.eles[ranVal-1].style.backgroundColor ='green';
    }
    else{
        message.innerHTML = `Lost sorry you did not bet on ${ranVal}`; //player lost
        game.eles[ranVal-1].style.backgroundColor ='purple';
    }
    game.sel = []; //resets the game selection array
    updateScore(); //updates the score +- winnings/loses

    game.eles.forEach((el)=>{
        el.bet = false;
    }) //resets game elements to false

}


function createBoard(){
    for(let i=0;i<total;i++){
        const temp = createEle(output,'div',`${i+1}`,'box');
        if(i%2){
            temp.style.backgroundColor = 'red';
        }else{
            temp.style.backgroundColor = 'black';  
            temp.style.color = 'white';
        }
        game.eles.push(temp);
        temp.bet = false;
        temp.addEventListener('click',(e)=>{
            btn.disabled = false; //allows to play again after making bet
            if(game.winner){ //game winner index value
                const parTemp = game.eles[game.winner];
                parTemp.style.backgroundColor = game.styler[0];
                parTemp.style.color = game.styler[1];  //used to store the color to reset background colors
                game.winner = false;
                const bets = parTemp.querySelector('.bet');
                if(bets){
                    bets.remove(); //resets bets
                }
            }
            console.log(temp.textContent);
            if(temp.bet){
                console.log(game.winner);
                const bets = temp.querySelector('.bet');
                bets.remove();
                //console.log(bets);
                temp.bet = false;
                game.coins++; //adds coins to the game
                const index = game.sel.indexOf(i+1);
                if(index > -1){
                    game.sel.splice(index,1);
                }
            }
            else{
                game.sel.push(i+1);
                game.coins--;
                temp.bet = true;
                createEle(temp,'div','$','bet');
            }
            updateScore();
        },true);
    }
    output.style.setProperty(`grid-template-columns`,`repeat(${game.x},1fr)`)
}




function updateScore(){
    score.innerHTML = `Coins : ${game.coins}`;
    console.log(game.sel);
}


function createEle(parent,eleType,html,eleClass){
    const ele = document.createElement(eleType);
    ele.innerHTML = html;
    ele.classList.add(eleClass);
    return parent.appendChild(ele);
}