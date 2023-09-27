document.addEventListener("DOMContentLoaded", function() {
    const imageInput = document.querySelector("#imageInput");
    const responseContainer = document.querySelector("#responseContainer");
    const register = document.querySelector("#register");
    const login = document.querySelector("#login")
    const loginContainer = document.querySelector("#loginContainer")
    const registerContainer = document.querySelector("#registerContainer");
    const uploadFormButton = document.querySelector("#upload");
    const uploadContainer = document.querySelector("#uploadContainer");
    const uploadForm = document.querySelector("#uploadForm");
    const registerForm = document.querySelector("#registerForm");
    const loginForm = document.querySelector("#loginForm");
    const logoutButton = document.querySelector("#logoutButton");


    // Navbar Button configuerations starts
    register.addEventListener("click", function () {
        registerContainer.classList.remove("hidden");
        loginContainer.classList.add("hidden");
        uploadContainer.classList.add("hidden");
        console.log(localStorage)
    });

    login.addEventListener("click", function () {
        registerContainer.classList.add("hidden");
        loginContainer.classList.remove("hidden");
        uploadContainer.classList.add("hidden");
    });
    uploadFormButton.addEventListener("click", function (){
        registerContainer.classList.add("hidden");
        loginContainer.classList.add("hidden");
        uploadContainer.classList.remove("hidden");
    });


    // Navbar Button configuerations ends

    //Register Form working
    registerForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(registerForm);
        fetch("http://localhost:8000/api/register/", {
            method : "POST",
            body : formData,
        })
        .then(response => {
            if (response.ok) {
                console.log("Register Successful!");
            } else {
                console.error("Register Failed!");
            }
        })
        .catch(error => {
            console.error("Network Error: ", error);
        });
    });


    //Login form working
    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData(loginForm);

        fetch("http://localhost:8000/api/login/", {
            method : "POST",
            body : formData,
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                console.error("Login Failed!");
                return null;
            }
        })
        .then(data => {
            if (data && data.token) {
                localStorage.setItem("token", data.token);
                console.log("login successful!");
            }
        })
        .catch(error => {
            console.error("Network Error: ", error);
        });
    });




    //Image Upload and sending to api server functionality
    uploadForm.addEventListener("submit", function (event) {
        event.preventDefault();
        
        const formData = new FormData();
        formData.append("image", imageInput.files[0]);

        fetch("http://localhost:8000/api/upload_image/", {
            method : "POST",
            body : formData,
        })
        .then(response => {
            if(response.ok) {
                resp = response.json();
                return resp;
            } else {
                console.error("Error uploading image")
            }
        })
        .then(data => {
            responseContainer.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error("Network error : ", error)
        });
    });
});