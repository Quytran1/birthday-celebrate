const backgroundMusic = document.getElementById('background-music');

// Phát nhạc khi người dùng nhấn vào trang
document.body.addEventListener('click', () => {
  if (backgroundMusic.paused) {
    backgroundMusic.play().catch(err => {
      console.error('Failed to play music:', err);
    });
  }
});
let firstSlideContainer = 
document.getElementsByClassName("slide--content")[0];

let secondSlideContainer = 
document.getElementsByClassName("slide--content--one")[0];

let secondCanvas = 
document.getElementsByClassName("second--canvas")[0];

secondSlideContainer.setAttribute("style","display:none");
secondCanvas.setAttribute("style","display:none");

let thirdCanvas = 
document.getElementsByClassName("third--canvas")[0];

thirdCanvas.setAttribute("style","display:none");



let containerToggleOne = setTimeout(function(){
	firstSlideContainer.setAttribute("style","display:none");
	secondSlideContainer.setAttribute("style","display:block");
},2000);


let removeFirstSlide = setTimeout(function(){
	document.getElementsByClassName("first--slide")[0].setAttribute("style","display:none;")
	secondCanvas.setAttribute("style","display:block");
},8500);

let removeSecondCanvas = setTimeout(function(){
	secondCanvas.setAttribute("style","display:none");
	thirdCanvas.setAttribute("style","display:block")
},13800)
