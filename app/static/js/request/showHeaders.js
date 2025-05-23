const data = JSON.parse(localStorage.getItem("excelData"));
const primeraHoja = data ? Object.keys(data)[0] : null;
console.log(primeraHoja ? data[primeraHoja] : null);
const registro_columnas = primeraHoja ? data[primeraHoja] : null;


console.log("entardnof al archivo")

if (registro_columnas && registro_columnas.length > 0) {
    const headers = Object.keys(registro_columnas[0]);

    const contentOpciones = document.getElementById('content-opciones-columnas')

    headers.forEach(header => {
    const option = document.createElement("option");
    option.textContent = `<{{ ${header} }}>`;
    contentOpciones.appendChild(option);
    console.log(header)
    });
}


const selectElement = document.getElementById('content-opciones-columnas');

function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(function() {
            console.log('Texto copiado al portapapeles:', text);
        }).catch(function(err) {
            console.error('Error al copiar el texto: ', err);
        });
    }


    selectElement.addEventListener('change', function() {
        const selectedValue = this.value; 
        
        if (selectedValue && selectedValue !== "selecciona una variable") {
            copyToClipboard(selectedValue);
        }
    });
