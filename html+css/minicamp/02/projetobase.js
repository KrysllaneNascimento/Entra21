var board = []
var currentGame = [1, 5, 11, 13, 15, 17]
var savedGames = []
var state = {board: [], currentGame: [], savedGames: []}

function start(){
    addNumberToGame(1)
    addNumberToGame(2)
    addNumberToGame(3)
    addNumberToGame(4)
    addNumberToGame(5)
    addNumberToGame(8)
    addNumberToGame(8)
    console.log(state.currentGame)
    
}

function addNumberToGame(numberToAdd){
    if (numberToAdd <1 || numberToAdd > 60){
        console.error('Número inválido', numberToAdd)
        return
    }
    if (state.currentGame.length >= 6){
        console.error('O jogo já está completo')
        return
    }
    if (isNumberInGame(numberToAdd)){
        console.error('Este número já está no jogo', numberToAdd)
    }

    state.currentGame.push(numberToAdd)
}
function isNumberInGame(numberToCheck){
    return state.currentGame.includes(numberToCheck)

}

start()