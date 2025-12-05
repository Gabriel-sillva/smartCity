import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Inicial } from "../Paginas/Inicial";
import { Login } from "../Paginas/Login";
import { Ambientes } from "../Paginas/Ambientes";
import { Sensores } from "../Paginas/Sensores";
import { Historicos } from "../Paginas/Historicos";
import ProtectedRoute from "../Componentes/ProtectedRoute";

export default function Rotas() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />

        <Route path="/" element={
          <ProtectedRoute><Inicial /></ProtectedRoute>
        } />

        <Route path="/ambientes" element={
          <ProtectedRoute><Ambientes /></ProtectedRoute>
        } />

        <Route path="/sensores" element={
          <ProtectedRoute><Sensores /></ProtectedRoute>
        } />

        <Route path="/historicos" element={
          <ProtectedRoute><Historicos /></ProtectedRoute>
        } />
      </Routes>
    </BrowserRouter>
  );
}
