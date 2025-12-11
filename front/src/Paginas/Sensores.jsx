import axios from "axios";
import React, { useEffect, useState } from "react";
import estilo from "./sensores.module.css";

export function Sensores() {

    const [ambientes, setAmbientes] = useState([]);

    useEffect(() => {

        const token = localStorage.getItem('access_token');

        if (!token) {
            console.warn("Nenhum token encontrado no localStorage.");
            return;
        }

        axios.get('http://localhost:8000/api/sensores/', {
            headers: { 
                'Authorization': `Bearer ${token}` 
            }
        })
        .then(response => {
            setAmbientes(response.data);
            console.log("Sensores carregados:", response.data);
        })
        .catch(error => console.error('Erro ao buscar sensores:', error));

    }, []);

    console.log("Estado atual de sensores:", Sensores);

    return (
        <div className={estilo["table-container"]}>
            <table className={estilo["table-ambientes"]}>
                
                <thead>
                    <tr>
                        <th>Tipo</th>
                        <th>MAC Address</th>
                        <th>Unidade</th>
                        <th>Latitude</th>
                        <th>Longitude</th>
                        <th>Status</th>
                        <th>Criado</th>
                        <th>ID Ambiente</th>
                    </tr>
                </thead>

                <tbody>
                    {ambientes.map((sensor) => (
                        <tr key={sensor.id}>
                            <td>{sensor.tipo}</td>
                            <td>{sensor.mac_address}</td>
                            <td>{sensor.unidade_media}</td>
                            <td>{sensor.latitude}</td>
                            <td>{sensor.longitude}</td>
                            <td>{sensor.status}</td>
                            <td>{sensor.criado_em}</td>
                            <td>{sensor.ambiente.id}</td>
                        </tr>
                    ))}
                </tbody>

            </table>
        </div>
    );
}
