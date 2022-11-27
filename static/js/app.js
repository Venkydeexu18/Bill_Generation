import mandals from "./mandals.js";
import designations from "./designations.js";
const container = document.getElementById("mandalsContainer");
const designationsContainer = document.getElementById("designations");
const minp = document.getElementById("mandals");
const des = document.getElementById("des");
const download = document.getElementById("download");

if(download != undefined){
    download.addEventListener("click", () => {
        var doc = new jsPDF;
        html2canvas(document.querySelector("#pdfcont")).then(canvas => {
            doc.addImage(canvas, 0, 0);
            doc.save(`${document.getElementById("rec").textContent}.pdf`)
            window.location.href='/'
        });
    })
}

mandals.forEach((mandal) => {
    const option = document.createElement('p');
    option.classList.add("dropitem");
    option.textContent = mandal.mandal;
    option.addEventListener("click", (e) => {
        e.preventDefault();
        minp.value = mandal.mandal;
        container.style.display = "none"
    })
    container.appendChild(option);
})


designations.forEach((employee) => {
    const option = document.createElement('p');
    option.classList.add("dropitem");
    option.textContent = employee.designation;
    option.addEventListener("click", (e) => {
        e.preventDefault();
        des.value = employee.designation;
        designationsContainer.style.display = "none"
    })
    designationsContainer.appendChild(option);
})

minp.addEventListener("click", (e) => {
    e.preventDefault();
    container.style.display = "flex"
})


des.addEventListener("click", (e) => {
    e.preventDefault();
    designationsContainer.style.display = "flex"
})


