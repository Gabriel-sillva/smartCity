// src/Componentes/Cabecalho.jsx
import { useNavigate } from "react-router-dom";
import { logout } from "../services/auth";
import styles from "./Cabecalho.module.css";

export default function Cabecalho() {
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate("/login");
  }

  return (
    <header className={styles.header}>
      <div className={styles.brand} onClick={() => navigate("/")}>SmartCity</div>
      <div>
        <button className={styles.btn} onClick={() => navigate("/historicos")}>Histórico</button>
        <button className={styles.btn} onClick={() => navigate("/ambientes")}>Ambientes</button>
        <button className={styles.btn} onClick={() => navigate("/sensores")}>Sensores</button>
        <button className={styles.btnDanger} onClick={handleLogout}>Logout</button>
      </div>
    </header>
  );
}
