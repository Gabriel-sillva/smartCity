import { Link } from "react-router-dom";
import estilo from "./Cabecalho.module.css";
import logo from "../assets/logo.png";

export function Cabecalho() {
  return (
    <header className={estilo.header}>
      {/* Esquerda: Home */}
      <div className={estilo.left}>
        <Link to="/inicial" className={estilo.navItem}>Home</Link>
      </div>

      {/* Centro: Logo */}
      <div className={estilo.center}>
        <img src={logo} alt="Logo SmartCity" className={estilo.logo} />
      </div>

      {/* Direita: Botões */}
      <nav className={estilo.right}>
        <Link to="/inicial/ambientes" className={estilo.navItem}>Ambientes</Link>
        <Link to="/inicial/sensores" className={estilo.navItem}>Sensores</Link>
        <Link to="/inicial/historicos" className={estilo.navItem}>Histórico</Link>
      </nav>
    </header>
  );
}
