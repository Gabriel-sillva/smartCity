// src/services/auth.js
import api, { setAuthToken } from "./api";

export async function loginRequest(username, password) {
  const res = await api.post("token/", { username, password });
  // res.data: { access, refresh }
  setAuthToken(res.data.access);
  localStorage.setItem("refresh_token", res.data.refresh);
  return res.data;
}

export function logout() {
  setAuthToken(null);
  localStorage.removeItem("refresh_token");
}

export function isAuthenticated() {
  return !!localStorage.getItem("access_token");
}
