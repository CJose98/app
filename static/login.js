/*  *** REGISTRAR *** */
let registro=document.getElementById('registro');  //http://127.0.0.1:5000/auth/login
registro.addEventListener('click', function(){

    window.location.href = "/auth/registro";     // "registro.html"; // "/auth/user_logeado";

}); 

 /* *** LOGIN *** */
document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    login();
});


function login() {
    const data = {
        correo: document.getElementById("correo").value,
        password: document.getElementById("password").value,
    };

    console.log("Datos del formulario:", data); /*ayuda en consola */

    fetch("http://127.0.0.1:5000/auth/login", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include'
    })
    .then(response => {
        console.log("Respuesta del servidor:", response);

        if (response.status === 200) {
            // Redirect to profile page if login is successful
            return response.json().then(data => {
                console.log("Datos de respuesta (éxito):", data);
                window.location.href = "/auth/user_logeado"; //"user_logeado.html";  //  "../templates/user_logeado.html";  //"user_logeado.html"; //"../templates/user_logeado.html";          //window.location.href = "/auth/user_logeado.html";
            });
        } else {
            return response.json().then(data => {
                console.log("Datos de respuesta (error):", data);
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}