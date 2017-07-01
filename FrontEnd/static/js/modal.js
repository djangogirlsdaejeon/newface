var modalBackground = document.querySelector("#modal-background");
var modalContainer = document.querySelector("#modal-container");

function openModal() {

    modalContainer.style.visibility = "visible";
    modalBackground.style.visibility = "visible";
}

modalBackground.addEventListener('click', () => {
    modalBackground.style.visibility = "hidden";
    modalContainer.style.visibility = "hidden";
});

