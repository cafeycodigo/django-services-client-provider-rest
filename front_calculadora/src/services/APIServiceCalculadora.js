const URL_API = 'http://localhost:8001/api/calculadora'

// Servicio que conecta React con las operaciones del Sistema B.
const APIServiceCalculadora = {
  async calcular(operacion, numero1, numero2) {
    const parametros = new URLSearchParams({ numero_1: numero1, numero_2: numero2 })
    const respuesta = await fetch(`${URL_API}/${operacion}/?${parametros}`)
    const datos = await respuesta.json()
    if (!respuesta.ok) throw new Error(datos.error || 'La API devolvió un error')
    return datos
  },
}

export default APIServiceCalculadora
