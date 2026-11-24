// ================================================================
//  AeroLista ✈ · main.js  —  el "director de orquesta"
//  Versión 6: también actualiza el tablero.
// ================================================================

const estado = {
  vuelo: null,          // los datos del avión
  vista: "3d",          // "3d" o "2d"
  reservas: [],         // la lista de pasajeros (en orden de llegada)
  porAsiento: {},       // atajo para pintar: { "7D": pasajero, ... }
  seleccionado: null,   // asiento libre elegido con clic (🟡)
  encontrado: null,     // asiento resaltado por una búsqueda (🔵)
  enEdicion: null,      // pasajero que se está modificando (paso 20)
  pestana: "reservar",  // pestaña abierta del panel (paso 18)
  filtroClase: "",      // filtro de la pestaña Listar (paso 23)
};

async function refrescar(numeroNuevo = null) {
  await cargarReservas();                 // pide la lista y pinta el avión (semaforo.js)
  await cargarResumen();                  // 🆕 actualiza los números del tablero (tablero.js)
}

async function iniciar() {
  const r = await API.vuelo();
  if (!r.ok) {
    avisar(r.mensaje, "codigo");
    return;
  }
  estado.vuelo = r.datos;
  dibujarAvion();
  aplicarAngulos();
  await refrescar();
  avisar(`Vuelo ${estado.vuelo.codigo} listo · haz clic en un asiento`);
}

iniciar();
