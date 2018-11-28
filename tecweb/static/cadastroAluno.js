function notNull(){
  var getName = document.getElementById("name");
  var getNick = document.getElementById("nickname")
  var getUser = document.getElementById("user")
  var getBirth = document.getElementById("birthdate")
  var getEmail = document.getElementById("email")

  if (getName.value === " " || getName.value === null || getName.value === "" ){
    alert("Preencha todos os campos obrigatórios!")
  }
  if (getNick.value === " " || getNick.value === null || getNick.value === "" ){
    alert("Preencha todos os campos obrigatórios!")
  }
  if (getUser.value === " " || getUser.value === null || getUser.value === "" ){
    alert("Preencha todos os campos obrigatórios!")
  }
  if (getBirth.value === " " || getBIrth.value === null || getBirth.value === "" ){
    alert("Preencha todos os campos obrigatórios!")
  }

  if (getEmail.value === " " || getEmail.value === null || getEmail.value === "" ){
    alert("Preencha todos os campos obrigatórios!")
  }
};
