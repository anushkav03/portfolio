// elements 
const audioPlayer = document.getElementById("global-audio");


// functions
function playMusic(trackURL) {
    audioPlayer.src = trackURL
    audioPlayer.play()
}

function pauseMusic() {
    audioPlayer.pause()
}