// src/Paginas/Historicos.jsx
import { useEffect, useState } from "react";
import api from "../services/api";
import Cabecalho from "../Componentes/Cabecalho";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend, Title
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend, Title);

export default function Historicos() {
  const [hours, setHours] = useState(24);
  const [historicos, setHistoricos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => { fetchRecente(); }, [hours]);

  async function fetchRecente() {
    setLoading(true);
    try {
      const res = await api.get(`historicos/recentes/?hours=${hours}`);
      setHistoricos(res.data);
    } catch (err) { console.error(err); }
    finally { setLoading(false); }
  }

  // preparar dados para gráfico (ex.: por sensor id)
  const grouped = {};
  historicos.forEach(h => {
    const sid = h.sensor?.id ?? "unknown";
    if (!grouped[sid]) grouped[sid] = [];
    grouped[sid].push(h);
  });

  const labels = historicos.map(h => new Date(h.timestamp).toLocaleString());

  const datasets = Object.keys(grouped).map((sid, idx) => ({
    label: `Sensor ${sid}`,
    data: grouped[sid].map(x => x.valor),
    fill: false,
    tension: 0.2,
  }));

  const data = { labels, datasets };

  return (
    <>
      <Cabecalho />
      <div style={{ padding: 16 }}>
        <h2>Históricos (últimas {hours}h)</h2>
        <label>Período:
          <select value={hours} onChange={(e) => setHours(Number(e.target.value))}>
            <option value={1}>1</option><option value={6}>6</option><option value={12}>12</option>
            <option value={24}>24</option><option value={72}>72</option>
          </select>
        </label>

        {loading ? <p>Carregando...</p> : (
          <>
            <div style={{ maxWidth: 900, marginTop: 20 }}>
              <Line data={data} />
            </div>

            <table>
              <thead>
                <tr><th>ID</th><th>Sensor</th><th>Ambiente</th><th>Valor</th><th>Timestamp</th></tr>
              </thead>
              <tbody>
                {historicos.map(h => (
                  <tr key={h.id}>
                    <td>{h.id}</td>
                    <td>{h.sensor?.id}</td>
                    <td>{h.ambiente?.descricao}</td>
                    <td>{h.valor}</td>
                    <td>{new Date(h.timestamp).toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </>
        )}
      </div>
    </>
  );
}
