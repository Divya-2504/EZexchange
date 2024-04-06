function collapsedMenu(id){
    if (screen.height > screen.width){
        if(id.style.display == "none" || id.style.display == ""){
            id.style.display = "block"
            // console.log("was none  ")
        }
        else{
            id.style.display="none";
            // console.log("eklse")
        }
        // console.log("port")
    }
}