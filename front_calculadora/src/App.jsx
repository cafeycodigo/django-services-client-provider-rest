import { useState } from 'react'
import APIServiceCalculadora from './services/APIServiceCalculadora'

const operaciones = ['suma', 'resta', 'multiplicacion', 'division']

function App() {
  const [numero1, setNumero1] = useState('')
  const [numero2, setNumero2] = useState('')
  const [operacion, setOperacion] = useState('suma')
  const [resultado, setResultado] = useState(null)
  const [error, setError] = useState('')

  async function ejecutarCalculo(evento) {
    evento.preventDefault()
    setError('')
    setResultado(null)
    try {
      setResultado(await APIServiceCalculadora.calcular(operacion, numero1, numero2))
    } catch (errorApi) {
      setError(errorApi.message)
    }
  }

  return (
    <main className="pagina">
      <section className="encabezado"><p>FRONT_CALCULADORA · REACT</p><h1>Calculadora conectada a una API</h1><span>Los cálculos se ejecutan en el Sistema B.</span></section>
      <section className="tarjeta">
        <form onSubmit={ejecutarCalculo}>
          <div className="campos"><label>Primer número<input type="number" value={numero1} onChange={(e) => setNumero1(e.target.value)} required /></label><label>Segundo número<input type="number" value={numero2} onChange={(e) => setNumero2(e.target.value)} required /></label></div>
          <label>Operación<select value={operacion} onChange={(e) => setOperacion(e.target.value)}>{operaciones.map((nombreOperacion) => <option key={nombreOperacion} value={nombreOperacion}>{nombreOperacion}</option>)}</select></label>
          <button type="submit">Calcular</button>
        </form>
        {resultado && <div className="resultado"><small>Resultado</small><strong>{resultado.resultado}</strong><span>{resultado.operacion}</span></div>}
        {error && <div className="error">{error}</div>}
      </section>
    </main>
  )
}

export default App
