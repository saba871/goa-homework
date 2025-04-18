const myForm = document.querySelector(".my-form");
const text = document.getElementById("text");
const email = document.getElementById("email");
const password = document.getElementById("password");

myForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const textValue = event.target.elements.text.value;
    const emailValue = event.target.elements.email.value;
    const passwordValue = event.target.elements.password.value;

    if (textValue === "" || emailValue === "" || passwordValue === "") {
        alert("Please fill out all fields.");
        return;
    }

    if (emailValue.length < 14) {
        alert("email is too short");
    }
    console.log(`Username: ${textValue}`);
    console.log(`Email: ${emailValue}`);
    console.log(`Pasword: ${passwordValue}`);

    event.target.reset();
});
// at მეთოდს ვიყენებთ იმისათვის რომ ამოვიღოთ სიიდან ელემენტი მარტივად
