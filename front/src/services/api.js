// src/services/api.js
import axios from "axios";

// baseURL = ajustar conforme seu back (use 8000 se for padrão)
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 15000,
});

export function setAuthToken(token) {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    localStorage.setItem("access_token", token);
  } else {
    delete api.defaults.headers.common["Authorization"];
    localStorage.removeItem("access_token");
  }
}

// inicializa a partir do storage se existir
const token = localStorage.getItem("access_token");
if (token) api.defaults.headers.common["Authorization"] = `Bearer ${token}`;

// Interceptor para 401 (token expirado)
api.interceptors.response.use(
  (resp) => resp,
  (error) => {
    if (error.response && error.response.status === 401) {
      // limpa token e força redirecionamento para login
      setAuthToken(null);
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);


// // exemplo frontend para baixar (se backend retornar blob)
// async function baixarXlsx() {
//   const res = await api.get("historicos/exportar/", { responseType: "blob" });
//   const url = window.URL.createObjectURL(new Blob([res.data]));
//   const link = document.createElement("a");
//   link.href = url;
//   link.setAttribute("download", "historicos.xlsx");
//   document.body.appendChild(link);
//   link.click();
//   link.remove();
// }



export default api;
