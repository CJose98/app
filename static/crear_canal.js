/* *** CREAR CANAL *** */
document.getElementById("Crear_Form_canal").addEventListener("submit", function (event) { 
    event.preventDefault();

    /***  ID SERVIDOR  ****/
    const id_servidor = localStorage.getItem('id_servidor');
    if (id_servidor) {

        console.log("ID del servidor:", id_servidor);
        
        Crear_canal(id_servidor);
    } else {
        console.error("ID del servidor no encontrado");
    }
    
});

function Crear_canal(id_servidor) {
    const data = {
        canal: document.getElementById("canal").value,
        id_servidor: id_servidor
    };

    console.log("Datos del formulario:", data); /*ayuda en consola */

    fetch("http://127.0.0.1:5000/auth/crear_canal", {
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