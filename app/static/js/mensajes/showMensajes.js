document.addEventListener('DOMContentLoaded', function() {
  const mensajesJSON = localStorage.getItem('mensajes');

  if (mensajesJSON) {
    try {
      const mensajes = JSON.parse(mensajesJSON);

      if (Array.isArray(mensajes)) {
        const mensajesContainer = document.querySelector('.row');

        if (mensajesContainer) {
          mensajes.forEach(textoMensaje => {
            const tieneMultiplesSaltos = /\n{2,}/.test(textoMensaje);
            const esLineaEnBlanco = /^\s*$/.test(textoMensaje);

            const colDiv = document.createElement('div');
            colDiv.classList.add('col-12', 'col-xl-4', 'd-flex', 'justify-content-center');

            const mensajeContenedorDiv = document.createElement('div');
            mensajeContenedorDiv.classList.add('mensaje-contenedor');

            const mensajeDiv = document.createElement('div');
            mensajeDiv.classList.add('mensaje');

            const mensajeContenidoDiv = document.createElement('div');
            mensajeContenidoDiv.classList.add('mensaje-contenido');

            const mensajeTextoP = document.createElement('p');
            mensajeTextoP.classList.add('mensaje-texto');
            mensajeTextoP.textContent = textoMensaje || 'Mensaje vacío';

            if (tieneMultiplesSaltos) {
              mensajeTextoP.classList.add('con-saltos-multiples'); // Agrega una clase para aplicar estilos específicos
            }
            if (esLineaEnBlanco) {
              mensajeTextoP.classList.add('linea-blanco'); // Agrega una clase para indicar línea en blanco
            }

            const mensajeMetadatosDiv = document.createElement('div');
            mensajeMetadatosDiv.classList.add('mensaje-metadatos');

            const mensajeHoraSpan = document.createElement('span');
            mensajeHoraSpan.classList.add('mensaje-hora');
            mensajeHoraSpan.textContent = '12:45';

            const mensajeEstadoSpan = document.createElement('span');
            mensajeEstadoSpan.classList.add('mensaje-estado', 'leido');
            const estadoIcon = document.createElement('i');
            estadoIcon.classList.add('bi', 'bi-check-all');
            mensajeEstadoSpan.appendChild(estadoIcon);

            mensajeMetadatosDiv.appendChild(mensajeHoraSpan);
            mensajeMetadatosDiv.appendChild(mensajeEstadoSpan);

            mensajeContenidoDiv.appendChild(mensajeTextoP);
            mensajeContenidoDiv.appendChild(mensajeMetadatosDiv);

            mensajeDiv.appendChild(mensajeContenidoDiv);
            mensajeContenedorDiv.appendChild(mensajeDiv);
            colDiv.appendChild(mensajeContenedorDiv);

            mensajesContainer.appendChild(colDiv);
          });
        } else {
          console.error('No se encontró el elemento con la clase "row".');
        }
      } else {
        console.log('No hay mensajes válidos en localStorage.');
      }
    } catch (error) {
      console.error('Error al parsear los mensajes de localStorage:', error);
    }
  } else {
    console.log('No se encontraron mensajes en localStorage.');
  }
});