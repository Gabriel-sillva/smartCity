import estilo from './Menu.module.css';
import { Link } from 'react-router-dom';

export function Menu() {
  return (
    <nav className={estilo.menuGrid}>
      <Link to='/' className={estilo.menuItem}>Home</Link>
      <Link to='/inicial/ambientes' className={estilo.menuItem}>Ambientes</Link>
      <Link to='/inicial/sensores' className={estilo.menuItem}>Sensores</Link>
      <Link to='/inicial/historicos' className={estilo.menuItem}>Historico</Link>
    </nav>
  );
}
