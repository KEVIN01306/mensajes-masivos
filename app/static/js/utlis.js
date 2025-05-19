export function obtenerDataExcel(){
    const data = JSON.parse(localStorage.getItem("excelData"));
    const primeraHoja = data ? Object.keys(data)[0] : null;
    console.log(primeraHoja ? data[primeraHoja] : null);
    return primeraHoja ? data[primeraHoja] : null;
}