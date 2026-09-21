var T_Voitures = [
  {
    immatriculation: "48-A-20000",
    marque: "Clio 3",
    couleur: "Noir",
    carburant: "Diesel",
    prixJour: 250,
  },
  {
    immatriculation: "48-A-20001",
    marque: "Clio 4",
    couleur: "Rouge",
    carburant: "Diesel",
    prixJour: 300,
  },
  {
    immatriculation: "48-A-20002",
    marque: "Dacia",
    couleur: "Noir",
    carburant: "Essence",
    prixJour: 200,
  },
];

function getAllVoitures() {
    var tableHTML =
      "<table border='1'><tr><th>Immatriculation</th><th>Marque</th><th>Couleur</th><th>Carburant</th><th>Prix/Jour</th></tr>";
  
    for (var i = 0; i < T_Voitures.length; i++) {
      tableHTML +=
        "<tr><td>" +
        T_Voitures[i].immatriculation +
        "</td><td>" +
        T_Voitures[i].marque +
        "</td><td>" +
        T_Voitures[i].couleur +
        "</td><td>" +
        T_Voitures[i].carburant +
        "</td><td>" +
        T_Voitures[i].prixJour +
        "</td><td><button class='delete-button' background-color ='red' onclick='deleteVoiture(\"" +
        T_Voitures[i].immatriculation +
        "\")'>Supprimer</button></td></tr>";
    }
  
    tableHTML += "</table>";
    document.body.innerHTML += tableHTML;
  }
  
  function deleteVoiture(immatriculation) {
    for (var i = 0; i < T_Voitures.length; i++) {
      if (T_Voitures[i].immatriculation === immatriculation) {
        T_Voitures.splice(i, 1);
        break;
      }
    }
  
    document.body.innerHTML = "";
    getAllVoitures();
  }
  
  function getVoitures(marque) {
    document.body.innerHTML = "";
  
    var filteredVoitures = T_Voitures.filter(function (voiture) {
      return voiture.marque === marque;
    });
  
    var tableHTML =
      "<table border='1'><tr><th>Immatriculation</th><th>Marque</th><th>Couleur</th><th>Carburant</th><th>Prix/Jour</th></tr>";
  
    for (var i = 0; i < filteredVoitures.length; i++) {
      tableHTML +=
        "<tr><td>" +
        filteredVoitures[i].immatriculation +
        "</td><td>" +
        filteredVoitures[i].marque +
        "</td><td>" +
        filteredVoitures[i].couleur +
        "</td><td>" +
        filteredVoitures[i].carburant +
        "</td><td>" +
        filteredVoitures[i].prixJour +
        "</td><td><button class='delete-button' background-color ='red' onclick='deleteVoiture(\"" +
        filteredVoitures[i].immatriculation +
        "\")'>Supprimer</button></td></tr>";
    }
  
    tableHTML += "</table>";
    document.body.innerHTML += tableHTML;
  }
  
  getAllVoitures();
  
  var form = document.createElement("form");
  
  // Create Label
  var label = document.createElement("label");
  label.textContent = "Marque :";
  label.setAttribute("for", "marque");
  
  // Create Input
  var input = document.createElement("input");
  input.type = "text";
  input.id = "marque";
  
  // Create Button
  var button = document.createElement("button");
  button.type = "button"; // Specify type as "button" to prevent form submission
  button.textContent = "Filter";
  button.onclick = function () {
    const marque_v = document.querySelector("#marque").value;
    getVoitures(marque_v);
  };
  
  // Append elements to the form
  form.appendChild(label);
  form.appendChild(input);
  form.appendChild(button);
  
  // Append the form to the body
  document.body.appendChild(form);