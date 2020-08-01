function edit(id) {
    console.log(id)

    document.getElementById(id).readOnly = false;

    console.log("out")
} 

function redirect(id){
    console.log(id)
    link = "/"+id;

    document.location.href=link;

}