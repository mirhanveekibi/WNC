document.addEventListener("DOMContentLoaded",()=>{
    var rightButton=document.querySelector("img#right");
    var leftButton=document.querySelector("img#left");
    var animalImage=document.querySelector("#animal-img");
    var animalImageNum=parseInt(animalImage.getAttribute("src").split("/")[4].replace(".png","")[1]);
    var animalImageLetter=animalImage.getAttribute("src").split("/")[4].replace(".png","")[0];

    uploadCircles(animalImageNum);

    rightButton.addEventListener("click",()=>{
        if(animalImageNum<5){
            animalImageNum+=1;
            animalImage.setAttribute("src",`../static/img/animals/${animalImageLetter}${animalImageNum}.png`);
            uploadCircles(animalImageNum);
        }else{
            animalImageNum=1;
            animalImage.setAttribute("src",`../static/img/animals/${animalImageLetter}${animalImageNum}.png`);
            uploadCircles(animalImageNum);
        }
    })

    leftButton.addEventListener("click",()=>{
        if(animalImageNum>1){
            animalImageNum-=1;
            animalImage.setAttribute("src",`../static/img/animals/${animalImageLetter}${animalImageNum}.png`);
            uploadCircles(animalImageNum);
        }else{
            animalImageNum=5;
            animalImage.setAttribute("src",`../static/img/animals/${animalImageLetter}${animalImageNum}.png`);
            uploadCircles(animalImageNum);
        }
    })
});

const uploadCircles=(num_variable)=>{
    let circles=document.querySelector(".circles>ul");
    let circleListItems=document.querySelectorAll(".circles>ul>li.circle");

    for(let i=0;i<circleListItems.length;i++){
        if(i==num_variable-1){
            circleListItems[i].classList.remove("non-selected");
            circleListItems[i].classList.add("selected");
        }else{
            circleListItems[i].classList.remove("selected");
            circleListItems[i].classList.add("non-selected");
        }
    }
};
