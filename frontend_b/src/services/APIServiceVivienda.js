const URL_BASE = 'http://localhost:8001/api/v2/viviendas/'

// Servicio responsable de comunicarse con la API de viviendas.
const APIServiceVivienda = {
  async listar() {
    const respuesta = await fetch(URL_BASE)
    if (!respuesta.ok) throw new Error('No fue posible cargar las viviendas')
    return respuesta.json()
  },

  async crear(datosVivienda) {
    return this.enviar(URL_BASE, 'POST', datosVivienda)
  },

  async actualizar(idVivienda, datosVivienda) {
    return this.enviar(`${URL_BASE}${idVivienda}/`, 'PUT', datosVivienda)
  },

  async eliminar(idVivienda) {
    const respuesta = await fetch(`${URL_BASE}${idVivienda}/`, { method: 'DELETE' })
    if (!respuesta.ok) throw new Error('No fue posible eliminar la vivienda')
  },

  async enviar(url, metodo, datos) {
    const respuesta = await fetch(url, {
      method: metodo,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos),
    })
    if (!respuesta.ok) throw new Error('La API rechazó la operación')
    return respuesta.json()
  },
}

export default APIServiceVivienda
