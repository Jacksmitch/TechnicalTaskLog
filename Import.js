// SOURCES
// For help creating code ChatGPT was used and modified


document.addEventListener('DOMContentLoaded', function () {

    // Fetch the JSON data from the external file
    fetch('TaskSheet.json')
        .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
        })
        .then(data => {

        // Your JSON data
        jsonData = data;

        // Get the table element
        var table = document.getElementById('jsonTable');

        // Create table header
        var header = table.createTHead();
        var headerRow = header.insertRow(0);
        for (var key in jsonData[0]) {
            var th = document.createElement('th');
            th.textContent = key;
            headerRow.appendChild(th);
        }
        
        // Create table body
        var tbody = table.createTBody();
        jsonData.forEach(function (item) {
            var row = tbody.insertRow();
            for (var key in item) {
                var cell = row.insertCell();
                if (item[key].includes("http")) {
                    // creating the link item for the markdown doc links
                    var link = document.createElement("a");
                    link.href = item[key];
                    link.innerHTML = item[key].split("/")[item[key].split("/").length - 1];
                    // add it into the cell of the table
                    cell.appendChild(link);
                }
                else {cell.textContent = item[key];}
            }
        });
        
        })
        .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        });
    
});