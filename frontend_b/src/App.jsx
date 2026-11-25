import { useEffect, useState } from 'react'
import APIServiceVivienda from './services/APIServiceVivienda'
import './App.css'

const viviendaInicial = {
  piso: '',
  numero: '',
  propietario: '',
}

function App() {
  const [viviendas, setViviendas] = useState([])
  const [vivienda, setVivienda] = useState(viviendaInicial)
  const [idEditando, setIdEditando] = useState(null)
  const [mensaje, setMensaje] = useState('')
  const [error, setError] = useState('')

  useEffect(() => {
    cargarViviendas()
  }, [])

  async function cargarViviendas() {
    try {
      setViviendas(await APIServiceVivienda.listar())
    } catch (errorCarga) {
      setError(errorCarga.message)
    }
  }

  function actualizarCampo(evento) {
    setVivienda({ ...vivienda, [evento.target.name]: evento.target.value })
  }

  async function guardarVivienda(evento) {
    evento.preventDefault()

    try {
      if (idEditando) {
        await APIServiceVivienda.actualizar(idEditando, vivienda)
        setMensaje('Vivienda actualizada correctamente.')
      } else {
        await APIServiceVivienda.crear(vivienda)
        setMensaje('Vivienda creada correctamente.')
      }

      cancelarEdicion()
      await cargarViviendas()
    } catch (errorGuardado) {
      setError(errorGuardado.message)
    }
  }

  function editarVivienda(viviendaSeleccionada) {
    setIdEditando(viviendaSeleccionada.id)
    setVivienda({
      piso: viviendaSeleccionada.piso,
      numero: viviendaSeleccionada.numero,
      propietario: viviendaSeleccionada.propietario,
    })
  }

  async function eliminarVivienda(idVivienda) {
    if (!window.confirm('¿Deseas eliminar esta vivienda?')) return

    try {
      await APIServiceVivienda.eliminar(idVivienda)
      setMensaje('Vivienda eliminada correctamente.')
      await cargarViviendas()
    } catch (errorEliminacion) {
      setError(errorEliminacion.message)
    }
  }

  function cancelarEdicion() {
    setIdEditando(null)
    setVivienda(viviendaInicial)
  }

  return (
    <main className="app">
      <header className="encabezado">
        <p className="etiqueta">Sistema B · API v2</p>
        <h1>Administración de viviendas</h1>
        <p>Gestiona las viviendas del condominio desde React.</p>
      </header>

      <section className="contenido">
        <form className="tarjeta formulario" onSubmit={guardarVivienda}>
          <h2>{idEditando ? 'Editar vivienda' : 'Nueva vivienda'}</h2>
          <label>Piso<input name="piso" type="number" value={vivienda.piso} onChange={actualizarCampo} required /></label>
          <label>Número<input name="numero" value={vivienda.numero} onChange={actualizarCampo} required /></label>
          <label>Propietario<input name="propietario" value={vivienda.propietario} onChange={actualizarCampo} required /></label>
          <div className="acciones-formulario">
            <button type="submit">{idEditando ? 'Guardar cambios' : 'Crear vivienda'}</button>
            {idEditando && <button type="button" className="boton-secundario" onClick={cancelarEdicion}>Cancelar</button>}
          </div>
        </form>

        <section className="tarjeta listado">
          <div className="titulo-listado"><div><p className="etiqueta">APIServiceVivienda</p><h2>Viviendas registradas</h2></div><span>{viviendas.length} registros</span></div>
          {mensaje && <div className="mensaje exito">{mensaje}</div>}
          {error && <div className="mensaje error">{error}</div>}
          <div className="tabla-contenedor"><table><thead><tr><th>Piso</th><th>Número</th><th>Propietario</th><th>Acciones</th></tr></thead><tbody>
            {viviendas.map((viviendaRegistrada) => (
              <tr key={viviendaRegistrada.id}>
                <td>{viviendaRegistrada.piso}</td><td>{viviendaRegistrada.numero}</td><td>{viviendaRegistrada.propietario}</td>
                <td className="acciones-tabla"><button onClick={() => editarVivienda(viviendaRegistrada)}>Editar</button><button className="boton-peligro" onClick={() => eliminarVivienda(viviendaRegistrada.id)}>Eliminar</button></td>
              </tr>
            ))}
          </tbody></table></div>
        </section>
      </section>
    </main>
  )
}

export default App
