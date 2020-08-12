function edit(id) {
    console.log(id);

    document.getElementById(id).classList.toggle("active");
    document.getElementById(id).onclick = false;
    document.getElementById(id).readOnly = false;

    save = "s"+id;
    document.getElementById(save).style.display = "inline";

    console.log("out");
} 

function redirect(id){
    console.log(id)
    link = "/"+id;

    document.location.href=link;

}