// ================================================================
//  AeroLista ✈ · clic.js — qué pasa al hacer clic en un asiento
//  Versión 1: solo enciende/apaga el amarillo y avisa.
// ================================================================

function clicEnAsiento(codigo) {
  const boton = botonDeAsiento(codigo);       // el <button> de ese asiento

  // toggle = interruptor: si el botón NO tiene la clase, se la pone; si la tiene, se la quita
  boton.classList.toggle("seleccionado");     // 🟡 encendido / apagado

  avisar(`Hiciste clic en el asiento ${codigo} · clase ${claseDeAsiento(codigo)}`);
}
