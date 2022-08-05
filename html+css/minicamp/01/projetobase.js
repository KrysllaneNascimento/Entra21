function calculateIMC(weight, height){
    return weight /(height * height)
}

function start(){
    buttonCalculateImc = document.querySelector('#button-calculate-imc')
    buttonCalculateImc.addEventListener('click', handleButtonClick)
    handleButtonClick()

    inputWeight = document.querySelector('#input-weight')
    inputHeight = document.querySelector('#input-height')

    inputHeight.addEventListener('input', handleButtonClick)
    inputWeight.addEventListener('input', handleButtonClick )
}

function handleButtonClick(){
    inputWeight = document.querySelector('#input-weight')
    inputHeight = document.querySelector('#input-height')
    imcResult = document.querySelector('#imc-result')

    height = Number(inputHeight.value)
    weight = Number(inputWeight.value)

    imc = calculateIMC(weight, height)

    formatedImc = imc.toFixed(2).replace('.',',')
    
    imcResult.textContent = formatedImc

}

start();
