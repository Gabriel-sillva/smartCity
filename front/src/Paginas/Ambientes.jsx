import axios from "axios";
import React, { useEffect, useState } from "react";
import estilo from "./Ambientes.module.css";

// ======================================================================
// Componente Ambientes
// ======================================================================
export function Ambientes() {

    // Estado que armazena a lista de ambientes
    const [ambientes, setAmbientes] = useState([]);

    // ==================================================================
    // useEffect — executa ao carregar a página
    // ==================================================================
    useEffect(() => {

        const token = localStorage.getItem('access_token');

        // Se não houver token, não tenta buscar
        if (!token) {
            console.warn("Nenhum token encontrado no localStorage.");
            return;
        }

        // Requisição GET para buscar ambientes
        axios.get('http://localhost:8000/api/ambientes/', {
            headers: { 
                'Authorization': `Bearer ${token}` 
            }
        })
        .then(response => {
            setAmbientes(response.data);
            console.log("Ambientes carregados:", response.data); // <-- OK AQUI
        })
        .catch(error => console.error('Erro ao buscar ambientes:', error));

    }, []);

    // Log **antes** do return também funciona sem erro
    console.log("Estado atual de ambientes:", ambientes);

    // ==================================================================
    // Renderização da Tabela
    // ==================================================================
    return (
        <div className={estilo["table-container"]}>
            <table className={estilo["table-ambientes"]}>
                
                <thead>
                    <tr>
                        <th>SIG</th>
                        <th>Descrição</th>
                        <th>Responsável</th>
                    </tr>
                </thead>

                <tbody>
                    {ambientes.map((ambiente) => (
                        <tr key={ambiente.id}>
                            <td>{ambiente.id}</td>
                            <td>{ambiente.descricao}</td>
                            <td>{ambiente.responsavel?.nome}</td>
                        </tr>
                    ))}
                </tbody>

            </table>
        </div>
    );
}
