/* ******************************       MOSTRAR SERVIDORES Y SALAS ******************************************** */

window.addEventListener('load', function () {
    getSala();
});

function getSala() {
    const url = "http://127.0.0.1:5000/auth/sala";

    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            let contenido = document.getElementById('contenido');
            contenido.style.display = 'none';

            // Parsear la respuesta como JSON
            return response.json();
        } 
        if (response.status === 200 && response.message === "Usuario no tiene servidores") {
            return document.getElementById("message").innerHTML = "Usuario no tiene servidores";

        } else {
            return response.json().then(data => {
                throw new Error("Response status not 200");
            });
        }
    })
    .then(data => {
        console.log("Datos del formulario_1:", data);
        const tabla = document.getElementById("tabla");
        
        for (const key in data) {
            if (data.hasOwnProperty(key)) { 
                const fila = tabla.insertRow();          
                const servidor = data[key]; 

                const nombreCelda = fila.insertCell(0); 
                nombreCelda.textContent = servidor.nombre_servidor;

                fila.addEventListener('click', function () {
                    const id = servidor.id_servidor;
                    localStorage.setItem('id_servidor', id);

                    // Agregar código para mostrar los canales aquí
                     mostrarCanales(id);

                });
        }};
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}

/****************************************************************************************** */

function mostrarCanales(id) {
    const url = `/auth/show_canal/${id}`;  /*`/auth/show_canal/${id}`   -- `http://127.0.0.1:5000/auth/show_canal/${id}` --    `http://127.0.0.1:5000/auth/servidor/${idServidor}/canales`; */

    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            // Parsear la respuesta como JSON
            return response.json();
        } 
        if (response.status === 200 && response.message === "Usuario no tiene canales") {
            return document.getElementById("message").innerHTML = "Usuario no tiene canales";

        } else {
            return response.json().then(data => {
                throw new Error("Response status not 200");
            });
        }
    })
    .then(data => {
        console.log("Datos del formulario_1:", data);

        let contenedor2 = document.getElementById('contenedor2');
        contenedor2.style.display = 'block';

        const tabla = document.getElementById("tabla_canal");
        tabla.innerHTML = "";
        
        for (const key in data) {
            if (data.hasOwnProperty(key)) { 
                const fila = tabla.insertRow();          
                const canales = data[key]; 

                const nombreCelda = fila.insertCell(0); 
                nombreCelda.textContent = canales.nombre_canal;

                fila.addEventListener('click', function () {
                    const id = canales.id_canal;

                    /*window.location.href = "/auth/show_canal/${id}";     // "registro.html"; // "/auth/user_logeado";*/

                    // Agregar código para mostrar los canales aquí
                    /*mostrarCanales(id);*/

                    /*let contenedor2 = document.getElementById('contenedor2');*/
                    /*contenedor2.style.display = 'block';*/

                });
                let salir = document.getElementById('salir');
                
                salir.addEventListener('click', function () {
                    tabla.innerHTML = "";
                    contenedor2.style.display = 'none';

                });

        }};
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}


/* CREAR SERVIDOR */
let sala_nueva=document.getElementById('sala_nueva');  //http://127.0.0.1:5000/auth/login
sala_nueva.addEventListener('click', function(){

    window.location.href = "/auth/crear_servidor";     // "registro.html"; // "/auth/user_logeado";

});   


/* CREAR CANAL */
let canal_nuevo=document.getElementById('c_canal');  //http://127.0.0.1:5000/auth/login
canal_nuevo.addEventListener('click', function(){

    window.location.href = "/auth/crear_canal";     // "registro.html"; // "/auth/user_logeado";

});









