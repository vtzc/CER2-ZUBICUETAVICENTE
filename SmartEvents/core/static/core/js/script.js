document.addEventListener("DOMContentLoaded", () => {
  const elemCuenta = document.querySelectorAll(".event-countdown");
  elemCuenta.forEach((elem) => {
    const fechaEventoStr = elem.dataset.eventDate;

    if (!fechaEventoStr) return;
    const fechaEvento = new Date(fechaEventoStr).getTime();
    const actuCuenta = setInterval(() => {
      const ahora = new Date().getTime();
      const dif = fechaEvento - ahora;

      if (dif < 0) {
        clearInterval(actuCuenta);
        elem.innerHTML = "¡El evento ha comenzado!";
        return;
      }

      const dias = Math.floor(dif / (1000 * 60 * 60 * 24));
      const horas = Math.floor((dif % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const min = Math.floor((dif % (1000 * 60 * 60)) / (1000 * 60));
      const seg = Math.floor((dif % (1000 * 60)) / 1000);
      elem.innerHTML = `${dias}d ${horas}h ${min}m ${seg}s`;}, 1000);
  });

  const formComentarios = document.getElementById("formulario_comentarios");
  const listaComentarios = document.getElementById("lista_comentarios");

  const mostrarComentarios = () => {
    const comentario = JSON.parse(localStorage.getItem("comentario")) || [];
    listaComentarios.innerHTML = "";

    comentario.forEach((comentario) => {
      const newComentario = document.createElement("div");
      newComentario.className = "card mb-3";
      newComentario.innerHTML = `
                <div class="card-body">
                    <h6 class="card-subtitle mb-2 text-muted">${comentario.nom} - ${comentario.fecha}</h6>
                    <p class="card-text">${comentario.msg}</p>
                </div>
            `;
      listaComentarios.prepend(newComentario);
    });
  };

  if (formComentarios) {
    formComentarios.addEventListener("submit", (event) => {
      event.preventDefault();

      const nom = document.getElementById("nom").value;
      const msg = document.getElementById("msg").value;
      const formFecha = new Date().toLocaleString("es-CL");

      const newCommentData = {
        nom: nom,
        msg: msg,
        fecha: formFecha,
      };

      const comentarios = JSON.parse(localStorage.getItem("comentario")) || [];
      comentarios.push(newCommentData);
      localStorage.setItem("comentario", JSON.stringify(comentarios));

      mostrarComentarios();

      formComentarios.reset();
    });
  }

  if (listaComentarios) {
    mostrarComentarios();
  }
});