let mensajes = [];

    const container = document.getElementById('textareaContainer');
    const btnAgregar = document.getElementById('addTextareaBtn');

    function cargarMensajes() {
        const guardado = localStorage.getItem('mensajes');
        if (guardado) {
            mensajes = JSON.parse(guardado);
            mensajes.forEach((texto, index) => {
                crearTextarea(index, texto);
            });
        } else {
            mensajes = [''];
            crearTextarea(0, '');
            guardarEnLocalStorage();
        }
    }
    function guardarEnLocalStorage() {
        localStorage.setItem('mensajes', JSON.stringify(mensajes));
    }

    function crearTextarea(index, valor = '') {
        const col = document.createElement('div');
        col.className = 'col-12 col-xl-4 p-2 card-write-mensaje';

        const textarea = document.createElement('textarea');
        textarea.className = 'shadow-box';
        textarea.setAttribute('data-index', index);
        textarea.value = valor;

        textarea.addEventListener('input', function() {
            mensajes[index] = this.value;
            guardarEnLocalStorage();
        });

        col.appendChild(textarea);
        container.appendChild(col);
    }

    btnAgregar.addEventListener('click', () => {
        const index = mensajes.length;
        mensajes.push('');
        crearTextarea(index, '');
        guardarEnLocalStorage();
    });

    // Borrar todo
    function borrarMensajes() {
        if (confirm('¿Estás seguro de que quieres borrar todos los mensajes?')) {
            localStorage.removeItem('mensajes');
            mensajes = [];
            container.innerHTML = '';
            mensajes.push('');
            crearTextarea(0, '');
            guardarEnLocalStorage();
        }
    }

    function borrarUltimoMensaje() {
        if (confirm('¿Estás seguro de que quieres borrar el último mensaje?')) {
            if (mensajes.length > 1) {
                mensajes.pop();

                localStorage.setItem('mensajes', JSON.stringify(mensajes));

                const container = document.getElementById('textareaContainer');
                if (container.lastElementChild) {
                    container.removeChild(container.lastElementChild);
                }
            } else {
                alert('Debe haber al menos un mensaje.');
            }
        }
    }

    window.onload = cargarMensajes;