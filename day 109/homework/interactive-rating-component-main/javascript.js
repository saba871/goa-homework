function simplefunction(){ // function
    document.getElementById("submit").addEventListener("click", () => {
        document.getElementsByClassName("container")[0].textContent = "thanks"
    })
}