let count = 1;
document.getElementById("radio1").checked = true;

setInterval( function(){
    nextImage();
}, 4000)

function nextImage(){
    count++;
    if(count>4){
        count = 1;
    }

    document.getElementById("radio" + count).checked = true;

}

function imgSlider(anything){
    document.querySelector('.starbucks').src = anything;

}
function changeCircleColor(color){
    const circle = document.querySelector('.circle');
    circle.style.background = color;
}