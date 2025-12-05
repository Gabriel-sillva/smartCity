// src/Paginas/Inicial.jsx
import Cabecalho from "../Componentes/Cabecalho";
import styles from "./Inicial.module.css";
import { useNavigate } from "react-router-dom";

export default function Inicial() {
  const navigate = useNavigate();

  return (
    <>
      <Cabecalho />
      <div className={styles.container}>
        <h1>Bem-vindo ao SmartCity</h1>
        <div className={styles.grid}>
          <button onClick={() => navigate("/sensores")}>Temperatura</button>
          <button onClick={() => navigate("/sensores")}>Umidade</button>
          <button onClick={() => navigate("/sensores")}>Luminosidade</button>
          <button onClick={() => navigate("/sensores")}>Contador</button>
        </div>
      </div>
    </>
  );
}
