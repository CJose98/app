window.addEventListener('load', function () {
    getCrearuser();
});

// document.getElementById("logout").addEventListener("click", logout);

function getCrearuser() {
    const url = "http://127.0.0.1:5000/auth/registro";
    
    fetch(url, {
        method: 'PUT',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {

                document.getElementById("email").innerText = data.correo;
                document.getElementById("username").innerText = data.nombre_usuario;
                document.getElementById("first_name").innerText = data.first_name;
                document.getElementById("last_name").innerText = data.last_name;
                document.getElementById("password").innerText = data.password;
                document.getElementById("dia").innerText = data.fecha_nac;
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}

function logout() {
    const url = "http://127.0.0.1:5000/auth/logout";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                window.location.href = "login.html";
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}
//#----en el btn crear canal llama a la funcion del model canal (crear modificar)
//el btn cerrar en el html de cada una vuelve a la pagina principal -----#/
btn_canal=document.getElementById('canal_new').addEventListener('click',function(){
    window.location.href = "/auth/crear_canal";
    Canal.crear_canal()
})
btn_mod_canal=document.getElementById('boton_mod').addEventListener('click', function(){
    Canal.mod_canal()
})
