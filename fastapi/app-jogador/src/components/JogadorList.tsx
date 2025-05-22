import React from "react";

interface Jogador {
  id?: string;
  nome: string;
  idade: number;
  time: string;
}

interface JogadorListProps {
  jogadores: Jogador[];
  onDeleteJogador: (id: string) => void;
  onEditJogador: (jogador: Jogador) => void;
}

const JogadorList: React.FC<JogadorListProps> = ({ jogadores, onDeleteJogador, onEditJogador }) => {
  return (
    <div>
      <h5 className="card text-center text-white bg-dark pb-1">
        Lista de Jogadores
      </h5>
      {jogadores.length > 0 ? (
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>Nome</th>
              <th>Idade</th>
              <th>Time</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {jogadores.map((jogador) => (

              <tr key={jogador.id || jogador.nome}>
                <td>{jogador.nome}</td>
                <td>{jogador.idade}</td>
                <td>{jogador.time}</td>
                <td>
                  <button
                    className="btn btn-sm btn-info me-2"
                    onClick={() => onEditJogador(jogador)}
                  >
                    Atualizar
                  </button>
                  <button
                    className="btn btn-sm btn-danger"
                    onClick={() => onDeleteJogador(jogador.id || '')}
                    disabled={!jogador.id}
                  >
                    Excluir
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Nenhum jogador cadastrado.</p>
      )}
    </div>
  );
};

export default JogadorList;