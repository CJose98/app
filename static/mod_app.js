/* *** MODIFICAR APELLIDO *** */
document.getElementById("Form_apellido").addEventListener("submit", function (event) {
    event.preventDefault();
    Modificar_apellido();
});


function Modificar_apellido() {
    const data = {
        n_foto: document.getElementById("n_apellido").value,
    };

    console.log("Datos del formulario:", data); /*ayuda en consola */

    fetch("http://127.0.0.1:5000/auth/editar_apellido", {
        method: 'PUT',
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


/*********************************************************************** */

/*  *** salir de la pantalla de modificar*** */
let volver_perfil=document.getElementById('volver_perfil');
volver_perfil.addEventListener('click', function(){

    window.location.href = "/auth/perfil_float";   

}); 