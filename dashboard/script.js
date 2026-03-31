fetch("stats.json")
.then(response => response.json())
.then(data => {

document.getElementById("emails").innerText = data.emails_sent;

document.getElementById("templateA").innerText = data.template_A;

document.getElementById("templateB").innerText = data.template_B;

document.getElementById("responses").innerText = data.responses;

document.getElementById("followups").innerText = data.followups;

})
.catch(error => console.log(error));
