import { useState } from 'react'
import APIPokemon from './services/APIPokemon'

function App() {
  const [nombre, setNombre] = useState('pikachu')
  const [pokemon, setPokemon] = useState(null)
  const [error, setError] = useState('')

  async function buscarPokemon(evento) {
    evento.preventDefault()
    setError('')

    try {
      setPokemon(await APIPokemon.buscar(nombre))
    } catch (errorApi) {
      setPokemon(null)
      setError(errorApi.message)
    }
  }

  return (
    <main>
      <header>
        <p>API_POKEMON · REACT</p>
        <h1>Buscador Pokémon</h1>
      </header>

      <form onSubmit={buscarPokemon}>
        <input
          value={nombre}
          onChange={(evento) => setNombre(evento.target.value)}
          placeholder="pikachu"
        />
        <button>Buscar</button>
      </form>

      {error && <div className="error">{error}</div>}

      {pokemon && (
        <article>
          <img src={pokemon.sprites.front_default} alt={pokemon.name} />
          <h2>{pokemon.name}</h2>
          <p>Altura: {pokemon.height}</p>
          <p>Peso: {pokemon.weight}</p>
          <p>Tipos: {pokemon.types.map((tipo) => tipo.type.name).join(', ')}</p>
        </article>
      )}
    </main>
  )
}

export default App
