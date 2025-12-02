import estilo from './Rodape.module.css';
import rodape_logo from '../assets/rodapesmartcity.png';

export function Rodape(){
    return(
        <footer className={estilo.rodape}>
            <h3>Tdos os direitos Reservados</h3>
             <img src={rodape_logo} alt="Logo Smartcity com cidade" className={estilo.rodape_logo}/>
        </footer>
    )
}