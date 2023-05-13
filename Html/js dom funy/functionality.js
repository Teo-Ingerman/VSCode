

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

        elements = Array.from(document.getElementsByClassName("big_button_green"))
        document.getElementById("time").style.color = "yellow"

        for (var i = 0; i < elements.length; i++){
            elements[i].className = "big_button_blue"
            
        }
    }

    else if (color === "black"){
        document.body.style.background = "green"; 

        elements = Array.from(document.getElementsByClassName("big_button_black"))
        document.getElementById("time").style.color = "#30d5c8"

        for (let i = 0; i < 9; i++){
            elements[i].className = "big_button_green"
        }

        
    }
    
    else if (color === "blue"){
        document.body.style.background = "black";

        elements = Array.from(document.getElementsByClassName("big_button_blue"))
        document.getElementById("time").style.color = "white"

        for (var i = 0; i < elements.length; i++){
            elements[i].className = "big_button_black"
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
    // alla bilder har samma namn och en siffra för sitt index
    // http://127.0.0.1:5500/Html/js%20dom%20funy/images/img4.png
    images = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png", "img6.png", "img7.png", "img8.png", "img9.png"]
    
    active_image = document.getElementById("the_image").src
    // tar bort extra text som hamnar framför bildens namn
    active_image = active_image.slice(50)
    index = images.indexOf(active_image)

    images.splice(index, 1)
    
    random_index = Math.floor(Math.random() * 8);

    new_image = images[random_index]
    document.getElementById("the_image").src=`images/${new_image}`;


}

function hide_picture(){
    document.getElementById("the_image").style.visibility = "hidden"
}

function show_picture(){
    document.getElementById("the_image").style.visibility = "visible"
}

function header(){
    other
}

function remove_header(){

}

function show_header(){

}