const form = document.querySelector("form");
const text = document.getElementById("text");
const email = document.getElementById("email");
const password = document.getElementById("pass");
const button = document.getElementById("btn");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    if (text.value == "" || email.value == "" || password == "") {
        alert("enter all form");
        return;
    }
    class User {
        constructor(text, email, password) {
            this._text = text;
            this._email = email;
            this._password = password;
        }
    }
    const userInfo = new User(text.value, email.value, password.value);
    console.log(userInfo);
});
