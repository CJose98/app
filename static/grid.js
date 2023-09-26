/* MOSTRAR GRID */
let todo_sala=document.getElementById('todo_sala');  //http://127.0.0.1:5000/auth/login
todo_sala.addEventListener('click', function(){
    
    
    let contenido = document.getElementById('contenido');
    /*let busqueda = document.getElementById('busqueda');*/
    const grid = document.querySelector('.grid-container'); 

    contenido.style.display = 'none';
    /*busqueda.style.display = 'block';*/
    grid.style.display = 'block';
}); 

