const URL_API_ACCESO = 'http://localhost:8000/api/v1/access/'

// Servicio responsable de registrar entradas y salidas en el Sistema A.
const APIServiceAcceso = {
  async registrar(datosAcceso) {
    const respuesta = await fetch(URL_API_ACCESO, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datosAcceso),
    })

    const resultado = await respuesta.json()
    if (!respuesta.ok && respuesta.status !== 403) {
      throw new Error(resultado.detail || 'No fue posible registrar el acceso')
    }
    return resultado
  },
}

export default APIServiceAcceso
