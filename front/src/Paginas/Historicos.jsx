import axios from "axios";
import React, { useEffect, useState } from "react";
import estilo from "./Historicos.module.css"; 

export function Historicos() {
  const [historico, setHistorico] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      console.warn("Nenhum token encontrado no localStorage.");
      return;
    }

    axios
      .get("http://localhost:8000/api/historicos/", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((response) => {
        setHistorico(response.data);
        console.log("Histórico carregado:", response.data);
      })
      .catch((error) => console.error("Erro ao buscar histórico:", error));
  }, []);

  return (
    <div className={estilo["table-container"]}>
      <table className={estilo["table-ambientes"]}>
        <thead>
          <tr>
            <th>Sensor</th>
            <th>Ambiente</th>
            <th>Valor</th>
            <th>Data / Hora</th>
          </tr>
        </thead>
        <tbody>
          {historico.map((item) => (
            <tr key={item.id}>
              <td>{item.sensor_tipo || item.sensor}</td>
              <td>{item.ambiente_descricao || item.ambiente}</td>
              <td>{item.valor}</td>
              <td>{new Date(item.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
