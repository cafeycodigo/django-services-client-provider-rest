const URL_API_POKEMON = 'http://localhost:8001/api/pokemon/'

const APIPokemon = {
  async buscar(nombrePokemon) {
    const respuesta = await fetch(`${URL_API_POKEMON}${nombrePokemon}/`)

    if (!respuesta.ok) {
      throw new Error('Pokémon no encontrado')
    }

    return respuesta.json()
  },
}

export default APIPokemon
