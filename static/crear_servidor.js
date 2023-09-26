  /* *** CREAR SERVIDOR *** */
document.getElementById("Crear_Form").addEventListener("submit", function (event) { 
    event.preventDefault();
    Crear_servidor();
});

function Crear_servidor() {
    const data = {
        servidor: document.getElementById("servidor").value,
    };

    console.log("Datos del formulario:", data); /*ayuda en consola */

    fetch("http://127.0.0.1:5000/auth/crear_servidor", {
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
                document.getElementById("message").innerHTML = data.message;

        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}

