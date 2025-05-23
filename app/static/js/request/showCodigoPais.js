const selectElement = document.getElementById('content-opciones-codigo-pais');

const opcionesDeCeldas = [
    { value: '502', nombreMostrar: 'Guatemala' },
    { value: '503', nombreMostrar: 'El Salvador' },
    { value: '504', nombreMostrar: 'Honduras' },
    { value: '505', nombreMostrar: 'Costa Rica' },
    { value: '506', nombreMostrar: 'Nicaragua' },
    { value: '507', nombreMostrar: 'Panamá' },
    
];

opcionesDeCeldas.forEach((opcionData,index )=> {
    const option = document.createElement('option');
    option.value = opcionData.value;
    option.textContent = opcionData.nombreMostrar;
    if (index === 0) {
        option.selected = true; 
    }
    selectElement.appendChild(option);
});