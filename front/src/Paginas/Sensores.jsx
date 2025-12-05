// src/Paginas/Sensores.jsx
import { useEffect, useState } from "react";
import api from "../services/api";
import Cabecalho from "../Componentes/Cabecalho";

export default function Sensores() {
  const [sensores, setSensores] = useState([]);
  const [filtro, setFiltro] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => { fetchSensores(); }, [filtro]);

  async function fetchSensores() {
    setLoading(true);
    try {
      const url = filtro ? `sensores/?tipo=${filtro}` : "sensores/";
      const res = await api.get(url);
      setSensores(res.data);
    } catch (err) { console.error(err); }
    finally { setLoading(false); }
  }

  async function toggleStatus(id) {
    try {
      await api.patch(`sensores/${id}/alterar_status/`);
      fetchSensores();
    } catch (err) { console.error(err); alert("Erro alterar status"); }
  }

  async function remover(id) {
    if (!confirm("Excluir sensor?")) return;
    try {
      await api.delete(`sensores/${id}/`);
      fetchSensores();
    } catch (err) { console.error(err); alert("Erro ao excluir"); }
  }

  return (
    <>
      <Cabecalho />
      <div style={{ padding: 16 }}>
        <h2>Sensores</h2>

        <label>Filtrar por tipo:
          <select value={filtro} onChange={(e) => setFiltro(e.target.value)}>
            <option value="">Todos</option>
            <option value="TEMP">Temperatura</option>
            <option value="UMI">Umidade</option>
            <option value="ILUM">Iluminação</option>
            <option value="CONT">Contador</option>
          </select>
        </label>

        {loading ? <p>Carregando...</p> : (
          <table>
            <thead>
              <tr><th>ID</th><th>Tipo</th><th>MAC</th><th>Unidade</th><th>Status</th><th>Ambiente</th><th>Ações</th></tr>
            </thead>
            <tbody>
              {sensores.map(s => (
                <tr key={s.id}>
                  <td>{s.id}</td>
                  <td>{s.tipo}</td>
                  <td>{s.mac_address}</td>
                  <td>{s.unidade_media}</td>
                  <td>{s.status}</td>
                  <td>{s.ambiente?.descricao}</td>
                  <td>
                    <button onClick={() => toggleStatus(s.id)}>Alternar</button>
                    <button onClick={() => remover(s.id)}>Excluir</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
