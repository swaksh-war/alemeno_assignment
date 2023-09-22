document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const imageInput = document.querySelector("#imageInput");
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
                console.log("Image uploaded successfully")
            } else {
                console.error("Error uploading image")
            }
        })
        .catch(error => {
            console.error("Network error : ", error)
        });
    });
});