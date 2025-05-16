document.getElementById("excel-form").addEventListener("submit", async function (e) {
    e.preventDefault(); // Evitar envío tradicional

    const formData = new FormData(this);

    const response = await fetch("/excel/", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    if (result.error) {
        window.location.href = "/";
        return;
    }

    localStorage.setItem("excelData", JSON.stringify(result.datos));

    window.location.href = "/validacion-data";
});