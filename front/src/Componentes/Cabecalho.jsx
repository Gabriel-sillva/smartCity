import estilo from './Cabecalho.module.css';
import logo from '..//assets/logosmartcity.jpg';

export function Cabecalho(){
    return(
        <header className={estilo.cabecalho}>
            <img src={logo} alt="Logo Smartcity" className={estilo.logo}/>
            <h1 className={estilo.titulo}>SmartCity</h1>
        </header>
    )
}