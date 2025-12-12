// src/Paginas/Home.jsx
import estilo from "./Home.module.css";

export function Home() {
  return (
    <>
     

      <main className={estilo.intro}>
        <h2 className={estilo.titulo}>Bem-vindo ao SmartCity</h2>
        <p className={estilo.texto}>
          O SmartCity é uma plataforma para monitoramento de ambientes,
          sensores e históricos em tempo real. Nosso objetivo é melhorar a
          infraestrutura urbana por meio de dados, promovendo eficiência,
          sustentabilidade e segurança.
        </p>

        <div className={estilo.gridHighlights}>
          <div className={estilo.card}>
            <h3 className={estilo.cardTitulo}>Ambientes</h3>
            <p className={estilo.cardTexto}>
              Gerencie laboratórios, salas e áreas monitoradas com dados atualizados.
            </p>
          </div>
          <div className={estilo.card}>
            <h3 className={estilo.cardTitulo}>Sensores</h3>
            <p className={estilo.cardTexto}>
              Acompanhe temperatura, umidade e outros indicadores essenciais.
            </p>
          </div>
          <div className={estilo.card}>
            <h3 className={estilo.cardTitulo}>Histórico</h3>
            <p className={estilo.cardTexto}>
              Analise tendências e gere insights para tomada de decisão.
            </p>
          </div>
        </div>
      </main>

      
    </>
  );
}
