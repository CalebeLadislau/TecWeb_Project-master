function notNull(){
    var getName = document.getElementById("inputName");
    var getData = document.getElementById("inputData");
    var getPlanoEnsino = document.getElementById("txtPlanoEnsino");
    var getCargaHoraria = document.getElementById("inputCargaHoraria");
    var getCompetencias = document.getElementById("txtCompetencias");
    var getHabilidade = document.getElementById("txtHabilidade");
    var getEmenta = document.getElementById("txtEmenta");
    var getBibliografiaBasica = document.getElementById("txtBibliografiaBasica");
    var getPercentualPratico = document.getElementById("inputPercentualPratico");
    var getPercentualToerico = document.getElementById("inputPercentualToerico");


    if (getName.value === " " || getName.value === null || getName.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }
    if (getData.value === " " || getData.value === null || getData.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }
    if (getPlanoEnsino.value === " " || getPlanoEnsino.value === null || getPlanoEnsino.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }
    if (getCargaHoraria.value === " " || getCargaHoraria.value === null || getCargaHoraria.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }

    if (getCompetencias.value === " " || getCompetencias.value === null || getCompetencias.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }

    if (getHabilidade.value === " " || getHabilidade.value === null || getHabilidade.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }

    if (getEmenta.value === " " || getEmenta.value === null || getEmenta.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }

    if (getBibliografiaBasica.value === " " || getBibliografiaBasica.value === null || getBibliografiaBasica.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }

    if (getPercentualPratico.value === " " || getPercentualPratico.value === null || getPercentualPratico.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }

    if (getPercentualToerico.value === " " || getPercentualToerico.value === null || getPercentualToerico.value === "" ){
        alert("Preencha todos os campos obrigatórios!");
    }


};


