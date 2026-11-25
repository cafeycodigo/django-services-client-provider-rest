const URL_API_RICK = 'http://localhost:8001/api/rick/characters/'

const APIRick = {
  async personajes() {
    const respuesta = await fetch(URL_API_RICK)

    if (!respuesta.ok) {
      throw new Error('No se pudieron cargar los personajes')
    }

    return respuesta.json()
  },
}

export default APIRick
