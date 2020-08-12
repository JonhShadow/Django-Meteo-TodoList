function validateForm(){ 
    document.getElementById("new").required = true;
} 

function validateForm2(){ 
    document.getElementById("new").required = false;
}

function edit(id) {
    console.log(id)
    date = 'd'+id;

    console.log(date);

    document.getElementById(id).readOnly = false;
    /*document.getElementById(date).readOnly = false;*/
    
    document.getElementById(id).classList.remove("Alta")
    document.getElementById(id).classList.remove("Media")
    document.getElementById(id).classList.remove("Baixa")

    document.getElementById(id).classList.toggle("active");

    console.log("out")
  } 

function prio(){
    console.log(name);
}


