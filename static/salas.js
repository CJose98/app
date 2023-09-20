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
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
                throw new Error("Response status not 200");
            });
        }
    })
    .then(data => {
        console.log("Datos del formulario_1:", data);
        const tabla = document.getElementById("tabla");

        //tabla.innerHTML = ""; // Limpiar la tabla antes de agregar datos

       // data.forEach((campo) => {
        for (const key in data) {
            if (data.hasOwnProperty(key)) { 
                const fila = tabla.insertRow();   
                const servidor = data[key]; 

                const nombreCelda = fila.insertCell(0); 
                nombreCelda.textContent = servidor.nombre_servidor;         
                  

                fila.addEventListener('click', function () {
                    const id = servidor.id_servidor;

                    let contenedor2 = document.getElementById('contenedor2');
                    contenedor2.style.display = 'block';

                });
        }};
    })
    .catch(error => {
        console.error("Error en la solicitud:", error);
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}

/*  *** contenido_de_busqueda y GRID *** */
let registro=document.getElementById('buscar_servidor');  //http://127.0.0.1:5000/auth/login
registro.addEventListener('click', function(){
    
    
    let contenido = document.getElementById('contenido');
    let busqueda = document.getElementById('busqueda');
    const grid = document.querySelector('.grid-container'); 

    contenido.style.display = 'none';
    busqueda.style.display = 'block';
    grid.style.display = 'block';
}); 










