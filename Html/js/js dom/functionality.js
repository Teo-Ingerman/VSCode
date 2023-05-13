// ändrar bakgrunden i början av programmet för att det ska kunna läsas av genom funktionen
document.body.style.background = "black"; 

setInterval(function(){
    // aktiverar funktionen time varje sekund
    time()
}, 1000);


  function time(){
    // tar informationen om vad tiden är
    // tar fram först året, månaden och dagen
    // tar fram timmar, minuter och sekunder sedan
    // lägger dem i p taggen med id time
    var today = new Date();
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds()
    date_time = date+' '+time;

    document.getElementById("time").innerHTML = date_time
}

function change_bg(){
    // läser av färgen som hemsidan har som bagrundsbild
    // ändrar sedan hemsidans bild beroende på vad färgen är
    let color = document.body.style.backgroundColor;

    if (color === "green"){
        document.body.style.background = "blue";
        elements = document.getElementsByClassName("big_button")
        document.getElementById("time").style.color = "yellow"

        for (var i = 0; i < elements.length; i++) {
            elements[i].className = "green_theme"
            // elements[i].style.color="blue";
            
        }
    }

    else if (color === "black"){
        document.body.style.background = "green"; 
        elements = document.getElementsByClassName("big_button")
        document.getElementById("time").style.color = "#30d5c8"

        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor="#30d5c8";
            elements[i].style.color="green";
        }

        
    }
    
    else if (color === "blue"){
        document.body.style.background = "black";
        elements = document.getElementsByClassName("big_button")
        document.getElementById("time").style.color = "white"
        
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor="white";
            elements[i].style.color="black";
        }
    }

}

function good_vibes(){
    // hittar ljudfilen som blev inladdad i htmldokumentet
    // startar musiken om den är pausad och pausar den om den spelar.
    const audio = document.querySelector("audio");
    if (audio.paused){
        audio.volume = 0.4;
        audio.play();
    }
    
    else{
        audio.pause()
    }

    
}

function time_button(){

    // ändrar stilelementet visibility i p taggen till motsatsen av vad det var innan
    visibility = document.getElementById("time").style.visibility

    if (visibility === "visible"){
        document.getElementById("time").style.visibility = "hidden"
    }

    else{
        document.getElementById("time").style.visibility = "visible"
    }
}

function change_picture(){

}

function hide_picture(){

}

function show_picture(){

}

function header(){

}

function remove_header(){

}

function show_header(){

}