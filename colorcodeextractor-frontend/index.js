document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const imageInput = document.querySelector("#imageInput");
    const responseContainer = document.querySelector("#responseContainer");
    form.addEventListener("submit", function (event) {
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