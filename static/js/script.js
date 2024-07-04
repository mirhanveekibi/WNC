document.addEventListener("DOMContentLoaded",()=>{
    var rightButton=document.querySelector("img#right");
    var leftButton=document.querySelector("img#left");
    var animalImage=document.querySelector("#animal-img");
    var animalImageNum=parseInt(animalImage.getAttribute("src").split("/")[4].replace(".png","")[1]);
    var animalImageLetter=animalImage.getAttribute("src").split("/")[4].replace(".png","")[0];

    rightButton.addEventListener("click",()=>{
        if(animalImageNum<5){
            animalImageNum+=1;
            animalImage.setAttribute("src",`../static/img/animals/${animalImageLetter}${animalImageNum}.png`);
        }
    })

    leftButton.addEventListener("click",()=>{
        if(animalImageNum>1){
            animalImageNum-=1;
            animalImage.setAttribute("src",`../static/img/animals/${animalImageLetter}${animalImageNum}.png`);
        }
    })
});

