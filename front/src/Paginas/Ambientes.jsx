// src/Paginas/Ambientes.jsx
import { useEffect, useState } from "react";
import api from "../services/api";
import Cabecalho from "../Componentes/Cabecalho";
import styles from "./Inicial.module.css";

export default function Ambientes() {
  const [ambientes, setAmbientes] = useState([]);
  const [descricao, setDescricao] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => { fetchAmbientes(); }, []);

  async function fetchAmbientes() {
    setLoading(true);
    try {
      const res = await api.get("ambientes/");
      setAmbientes(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  async function criarAmbiente(e) {
    e.preventDefault();
    try {
      // Ajuste local_id e responsavel_id conforme seu db (populacao automática costuma ter id 1)
      await api.post("ambientes/", { descricao, local_id: 1, responsavel_id: 1 });
      setDescricao("");
      fetchAmbientes();
    } catch (err) {
      console.error(err);
      alert("Erro ao criar ambiente");
    }
  }

  async function excluir(id) {
    if (!confirm("Excluir?")) return;
    try {
      await api.delete(`ambientes/${id}/`);
      fetchAmbientes();
    } catch (err) { console.error(err); alert("Erro ao excluir"); }
  }

  return (
    <>
      <Cabecalho />
      <div className={styles.container}>
        <h2>Ambientes</h2>

        <form onSubmit={criarAmbiente}>
          <input placeholder="Descrição" value={descricao} onChange={(e) => setDescricao(e.target.value)} required />
          <button type="submit">Criar</button>
        </form>

        {loading ? <p>Carregando...</p> : (
          <table>
            <thead>
              <tr><th>ID</th><th>Descrição</th><th>Local</th><th>Responsável</th><th>Ações</th></tr>
            </thead>
            <tbody>
              {ambientes.map(a => (
                <tr key={a.id}>
                  <td>{a.id}</td>
                  <td>{a.descricao}</td>
                  <td>{a.local?.nome}</td>
                  <td>{a.responsavel?.nome}</td>
                  <td><button onClick={() => excluir(a.id)}>Excluir</button></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
