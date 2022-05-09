function on(){
    document.getElementById("box").style.display="block";
}
function off(){
    document.getElementById("box").style.display="none";
}
function ps(){
    let k=document.getElementById("pas").value,h="c";
    if(k==h)
    {
        alert("correct");
        form.action="password.html";
     
    }
    else
    {
        alert("Incorrect");
    }
}
