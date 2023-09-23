window.addEventListener('load', function () {
    getProfile();
});

document.getElementById("logout").addEventListener("click", logout);

function getProfile() {
    const url = "http://127.0.0.1:5000/auth/profile";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {

                document.getElementById("username").innerText = data.username;
                document.getElementById("email").innerText = data.email;
                document.getElementById("first_name").innerText = data.first_name;
                document.getElementById("last_name").innerText = data.last_name;
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
    Canal.mod_canal();
})
//se agrega la funcion de eliminar crear modificar msg
btn_del_msg=document.getElementById('delete_canal').addEventListener('click',function(){
    Msg.eliminar_msg();
})
btn_mod_msg=document.getElementById('mod_msg').addEventListener('click'),function(){
    Msg.mod_msg();
}
btn_crear_msg=document.getElementById('crear_msg').addEventListener('click',function(){
    Msg.crear_msg();
})