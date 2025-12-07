import { Routes, Route } from "react-router-dom";
import { Menu } from '../Componentes/Menu';
import { Inicial } from "../Paginas/Inicial";
import { Login } from "../Paginas/Login";
import { Ambientes } from "../Paginas/Ambientes";

export function Rotas() {
    return (
        <Routes>

            {/* Página de Login */}
            <Route path="/" element={<Login />} />

            {/* Layout inicial */}
            <Route path="/inicial" element={<Inicial />}>

                {/* Conteúdo padrão ao entrar em /inicial */}
                <Route index element={<Menu />} />

                {/* Páginas internas */}
                <Route path="ambientes" element={<Ambientes />} />
                <Route path="sensores" element={<h2>Sensores</h2>} />

            </Route>
        </Routes>
    );
}
