window.addEventListener('load', function () {
    getProfile();
});


function getProfile() {
    const url = "http://127.0.0.1:5000/auth/mostrar_perfil";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                // Mostrar la imagen

                const imgElement = document.getElementById("img_perfil");
                imgElement.src =  data.img_perfil;    // Establece la URL como src
                imgElement.alt = "Imagen de perfil"; // Añade un atributo alt para descripción

                /*document.getElementById("img_perfil").innerText = data.img_perfil;*/
                document.getElementById("nombre_user").innerText = data.nombre_user;
                document.getElementById("nombre").innerText = data.nombre;
                document.getElementById("apellido").innerText = data.apellido;
                document.getElementById("correo").innerText = data.correo;
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







/************************************************************************ */

/*  *** salir de la pantatalla de perfil*** */
let volver_pantalla=document.getElementById('volver_pantalla');
volver_pantalla.addEventListener('click', function(){

    window.location.href = "/auth/user_logeado";   

}); 



/************************************************************************ */

/*  *** img_perfil *** */
let perfil=document.getElementById('perfil'); 
perfil.addEventListener('click', function(){

    window.location.href = "/auth/mod_img_perfil"; 
       

}); 
/*  *** nombre_user *** */
let user=document.getElementById('user');  
user.addEventListener('click', function(){

    window.location.href = "/auth/editar_user_name";     

}); 
/*  *** nombre *** */
let name=document.getElementById('name');  
name.addEventListener('click', function(){

    window.location.href = "/auth/editar_user";     

}); 
/*  *** apellido *** */
let last_name=document.getElementById('last_name');  
last_name.addEventListener('click', function(){

    window.location.href = "/auth/editar_apellido";    

}); 
/*  *** correo *** */
let email=document.getElementById('email');  
email.addEventListener('click', function(){

    window.location.href = "/auth/editar_correo";    

}); 
/*  *** password *** */
let password=document.getElementById('password'); 
password.addEventListener('click', function(){

    window.location.href = "/auth/editar_contraseña";    

}); 
