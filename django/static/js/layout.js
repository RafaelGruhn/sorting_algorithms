$(document).ready(function(){
  / Mensagens de alerta (com a classe desaparecer) irão desaparecer após 3 segundos. /
  if($(".desaparecer").is(':visible')){
    setTimeout(function(){
      $(".desaparecer").remove();
    }, 3000);
  }
});