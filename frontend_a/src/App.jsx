import { useState } from 'react'
import APIServiceAcceso from './services/APIServiceAcceso'

function App() {
  const [datosAcceso, setDatosAcceso] = useState({ plate: '', movement: 'entry' })
  const [resultado, setResultado] = useState(null)
  const [error, setError] = useState('')
  const [cargando, setCargando] = useState(false)

  function actualizarCampo(evento) {
    setDatosAcceso({ ...datosAcceso, [evento.target.name]: evento.target.value })
  }

  async function registrarAcceso(evento) {
    evento.preventDefault()
    setCargando(true)
    setError('')
    setResultado(null)

    try {
      setResultado(await APIServiceAcceso.registrar({ ...datosAcceso, plate: datosAcceso.plate.toUpperCase() }))
    } catch (errorRegistro) {
      setError(errorRegistro.message)
    } finally {
      setCargando(false)
    }
  }

  return (
    <main className="pagina">
      <section className="encabezado"><p>SISTEMA A · CONTROL DE ACCESO</p><h1>Entrada y salida de vehículos</h1><span>La patente será validada contra el Sistema B.</span></section>
      <section className="panel">
        <form onSubmit={registrarAcceso} className="tarjeta formulario"><h2>Registrar movimiento</h2><label>Patente<input name="plate" value={datosAcceso.plate} onChange={actualizarCampo} placeholder="ABCD12" required /></label><label>Movimiento<select name="movement" value={datosAcceso.movement} onChange={actualizarCampo}><option value="entry">Entrada</option><option value="exit">Salida</option></select></label><button disabled={cargando}>{cargando ? 'Consultando...' : 'Registrar acceso'}</button></form>
        <section className="tarjeta resultado"><h2>Resultado</h2>{error && <div className="alerta error">{error}</div>}{resultado && <div className={`alerta ${resultado.authorized ? 'exito' : 'error'}`}><strong>{resultado.authorized ? 'Acceso autorizado' : 'Acceso denegado'}</strong><p>Patente: {resultado.plate}</p>{resultado.vehicle?.house && <p>Vivienda: piso {resultado.vehicle.house.floor}, número {resultado.vehicle.house.number}<br />Propietario: {resultado.vehicle.house.owner}</p>}</div>}{!resultado && !error && <p className="vacio">Ingresa una patente para consultar el vehículo.</p>}</section>
      </section>
    </main>
  )
}

export default App
