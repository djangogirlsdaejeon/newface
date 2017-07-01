var modalBackground = document.querySelector("#boxhover");


function hoverModal(target){
    target.children[0].style.visibility = "visible"
    setTimeout(function(){
        unhoverModal(target);
    },2000);
}

function unhoverModal(target){
    target.children[0].style.visibility = "hidden";
}

function timeout(){
    setTimeout(function() {
       unhoverModal(); 
    }, 2000);
}

