const data = JSON.parse(localStorage.getItem("excelData"));
const primeraHoja = data ? Object.keys(data)[0] : null;
const registros = primeraHoja ? data[primeraHoja] : null;

if (registros && registros.length > 0) {
  const headers = Object.keys(registros[0]);

  const table = document.createElement("table");
  table.className = "tabla-estilo-excel"; 

  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");

  headers.forEach(header => {
    const th = document.createElement("th");
    th.textContent = header;
    headerRow.appendChild(th);
  });

  thead.appendChild(headerRow);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");

    registros.slice(0, 4).forEach(row => {
    const tr = document.createElement("tr");
    headers.forEach(header => {
        const td = document.createElement("td");
        td.textContent = row[header] ?? "";
        tr.appendChild(td);
    });
    tbody.appendChild(tr);
    });

  table.appendChild(tbody);
  document.getElementById("tabla-excel-container").appendChild(table);
} else {
  document.getElementById("tabla-excel-container").textContent = "No hay datos disponibles.";
}