var animateButton = function(e) {

  e.preventDefault;
  //reset animation
  e.target.classList.remove('animate');
  
  e.target.classList.add('animate');
  setTimeout(function(){
    e.target.classList.remove('animate');
  },700);
};

var bubblyButtons = document.getElementsByClassName("bubbly-button");
for (var i = 0; i < bubblyButtons.length; i++) {
  bubblyButtons[i].addEventListener('click', animateButton, false);
}







document.querySelector(".bubbly-button").addEventListener('click', () => {
  //recuperation de la fonction objectif
  const fonctionObjectif = document.querySelector(".js-fonction-objectif");
  let coeffFO = [];
  //savoir si on veut maximiser ou optimiser la f.o.
  const optimiser =fonctionObjectif.querySelector("select").value;
  console.log(optimiser);
  //valeur de a
  const a = fonctionObjectif.querySelector(".js-fo-inputx").value;
  if(a != ""){
    if(Number(a)){
      console.log(Number(a));
      coeffFO.push(Number(a));
    }else{
      fonctionObjectif.querySelector(".js-fo-inputx").value = '';
      alert("Les valeurs doivent être des nombres");
      return;
    }
  }else{
    console.log("le premier champ est vide");
    coeffFO.push(0);
  }
 

  //valeur de b 
  const b = fonctionObjectif.querySelector(".js-fo-inputy").value;
  if(b != ""){
    if(Number(b)){
      console.log(Number(b));
      coeffFO.push(Number(b));
    }else{
      fonctionObjectif.querySelector(".js-fo-inputy").value = '';
      alert("Les valeurs doivent être des nombres");
      return;
    }
  }else{
    console.log("le deuxieme champ est vide");
    coeffFO.push(0)
  }


  console.log("les coefficients de la fonction objectif sont: " + coeffFO);

  //recuperation des sous contraintes
  console.log("************");
  //va stocker les tabeux de sous-contraintes
  let coeff = [];
  document.querySelectorAll(".js-sous-contrainte").forEach((sousContrainte)  => {
    //va stocker les coefficients de chaque sous-contrainte
      let coeffSC = []
    sousContrainte.querySelectorAll("input").forEach((input) => {
      //console.log(Number(input.value));
      coeffSC.push(Number(input.value));
    })
    console.log(coeffSC);
    coeff.push(coeffSC);

  })
  console.log("les coefficients: ");
  console.log(coeff);
})
