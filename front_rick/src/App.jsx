import { useEffect, useState } from 'react'
import APIRick from './services/APIRick'

function App() {
  const [personajes, setPersonajes] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    APIRick.personajes()
      .then((datos) => setPersonajes(datos.results || []))
      .catch((errorApi) => setError(errorApi.message))
  }, [])

  return (
    <main>
      <header>
        <p>API_RICK · REACT</p>
        <h1>Personajes de Rick and Morty</h1>
      </header>

      {error && <div className="error">{error}</div>}

      <section className="grid">
        {personajes.map((personaje) => (
          <article key={personaje.id}>
            <img src={personaje.image} alt={personaje.name} />
            <h2>{personaje.name}</h2>
            <span>
              {personaje.status} · {personaje.species}
            </span>
          </article>
        ))}
      </section>
    </main>
  )
}

export default App
