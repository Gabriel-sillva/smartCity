import { Routes, Route } from "react-router-dom";
import { Inicial } from "../Paginas/Inicial";
import { Login } from "../Paginas/Login";
import { Home } from "../Paginas/Home";
import { Ambientes } from "../Paginas/Ambientes";
import { Sensores } from "../Paginas/Sensores";
import { Historicos } from "../Paginas/Historicos";

export function Rotas() {
  return (
    <Routes>
      {/* Rota principal para Login */}
      <Route path="/" element={<Login />} />

      {/* Rotas internas do sistema */}
      <Route path="/inicial" element={<Inicial />}>
        <Route index element={<Home />} />
        <Route path="ambientes" element={<Ambientes />} />
        <Route path="sensores" element={<Sensores />} />
        <Route path="historicos" element={<Historicos />} />
      </Route>
    </Routes>
  );
}
