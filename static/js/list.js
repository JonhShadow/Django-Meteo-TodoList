function validateForm(){ 
    document.getElementById("new").required = true;
} 

function validateForm2(){ 
    document.getElementById("new").required = false;
}

function edit(id) {
    console.log(id)
    document.getElementById(id).readOnly = false;
  } 

function prio(){
    name = {{ls.name}};
    console.log(name);
}


