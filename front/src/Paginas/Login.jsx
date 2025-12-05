import estilo from './Login.module.css';
import { useNavigate } from 'react-router-dom';
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from '@hookform/resolvers/zod';
import { useState } from "react";

const schemaLogin = z.object({
    username: z.string()
        .trim()
        .min(1, 'Informe um nome')
        .max(25, 'Máximo de 25 caracteres'),

    password: z.string()
        .trim()
        .min(1, 'Informe uma senha')
        .max(15, 'Máximo de 15 caracteres'),
});

export function Login() {
    const navigate = useNavigate();
    const [erroApi, setErroApi] = useState("");

    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm({
        resolver: zodResolver(schemaLogin),
    });

    async function enviarDados(data) {
        setErroApi("");

        try {
            const resposta = await fetch("http://localhost:8000/api/token/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });

            const resultado = await resposta.json();

            // Erro de autenticação
            if (!resposta.ok) {
                setErroApi("Usuário ou senha incorretos");
                return;
            }

            // Salvando tokens
            localStorage.setItem("access", resultado.access);
            localStorage.setItem("refresh", resultado.refresh);

            // Login OK -> vai para página inicial
            navigate("/");

        } catch (erro) {
            setErroApi("Erro ao conectar com o servidor");
            console.error("Erro:", erro);
        }
    }

    return (
        <section className={estilo.container}>
            <form className={estilo.formulario} onSubmit={handleSubmit(enviarDados)}>
                <h2 className={estilo.titulo}>Acesso ao Sistema</h2>

                {erroApi && <p className={estilo.erroApi}>{erroApi}</p>}

                <label htmlFor="usuario">Usuário:</label>
                <input
                    id="usuario"
                    type="text"
                    placeholder="Digite seu usuário"
                    {...register("username")}
                />
                {errors.username && (
                    <p className={estilo.erro}>{errors.username.message}</p>
                )}

                <label htmlFor="senha">Senha:</label>
                <input
                    id="senha"
                    type="password"
                    placeholder="Digite sua senha"
                    {...register("password")}
                />
                {errors.password && (
                    <p className={estilo.erro}>{errors.password.message}</p>
                )}

                <button className={estilo.botao}>Entrar</button>
            </form>
        </section>
    );
}
