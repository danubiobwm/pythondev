import React, { useState, useEffect, useCallback } from "react";
import "./App.css";
import axios from "axios";
import JogadorList from "./components/JogadorList";

interface Jogador {
  id?: string;
  nome: string;
  idade: number;
  time: string;
}

function App() {
  const [jogadorList, setjogadorList] = useState<Jogador[]>([]);
  const [nomeInput, setNomeInput] = useState<string>("");
  const [idadeInput, setIdadeInput] = useState<string>("");
  const [timeInput, setTimeInput] = useState<string>("");
  const [jogadorEditandoId, setJogadorEditandoId] = useState<string | null>(null);

  const fetchJogadores = useCallback(() => {
    axios
      .get("http://localhost:8000/jogadores")
      .then((response) => {
        if (response.data && Array.isArray(response.data.jogadores)) {
          setjogadorList(response.data.jogadores);
        } else if (response.data && Array.isArray(response.data)) {
          setjogadorList(response.data);
        } else {
          console.warn("Estrutura de dados inesperada da API:", response.data);
          setjogadorList([]);
        }
      })
      .catch((error) => {
        console.error("Erro ao buscar jogadores:", error);
      });
  }, []);

  useEffect(() => {
    fetchJogadores();
  }, [fetchJogadores]);

  const handleSubmitJogador = () => {
    if (!nomeInput || !idadeInput || !timeInput) {
      alert("Por favor, preencha todos os campos!");
      return;
    }

    const idadeNumerica = parseInt(idadeInput, 10);
    if (isNaN(idadeNumerica) || idadeNumerica <= 0) {
      alert("Por favor, insira uma idade válida (apenas números positivos).");
      return;
    }

    const jogadorData = {
      nome: nomeInput,
      idade: idadeNumerica,
      time: timeInput,
    };

    if (jogadorEditandoId) {
      axios
        .put(`http://localhost:8000/jogadores/${jogadorEditandoId}`, jogadorData)
        .then((response) => {
          alert("Jogador atualizado com sucesso!");
          console.log("Jogador atualizado:", response.data);
          limparFormulario();
          fetchJogadores();
        })
        .catch((error) => {
          console.error("Erro ao atualizar jogador:", error);
          alert("Erro ao atualizar jogador. Verifique o console para mais detalhes.");
        });
    } else {
      axios
        .post("http://localhost:8000/jogadores", jogadorData)
        .then((response) => {
          alert("Jogador adicionado com sucesso!");
          console.log("Jogador adicionado:", response.data);
          limparFormulario();
          fetchJogadores();
        })
        .catch((error) => {
          console.error("Erro ao adicionar jogador:", error);
          alert("Erro ao adicionar jogador. Verifique o console para mais detalhes.");
        });
    }
  };

  const limparFormulario = () => {
    setNomeInput("");
    setIdadeInput("");
    setTimeInput("");
    setJogadorEditandoId(null);
  };

  const handleDeleteJogador = useCallback((id: string) => {
    if (!id) {
      alert("ID do jogador não encontrado para exclusão.");
      return;
    }
    if (window.confirm("Tem certeza que deseja excluir este jogador?")) {
      axios
        .delete(`http://localhost:8000/jogadores/${id}`)
        .then(() => {
          alert("Jogador excluído com sucesso!");
          fetchJogadores();
        })
        .catch((error) => {
          console.error("Erro ao excluir jogador:", error);
          alert("Erro ao excluir jogador. Verifique o console para mais detalhes.");
        });
    }
  }, [fetchJogadores]);

  const handleEditJogador = useCallback((jogador: Jogador) => {
    setNomeInput(jogador.nome);
    setIdadeInput(String(jogador.idade));
    setTimeInput(jogador.time);
    setJogadorEditandoId(jogador.id || null);
  }, []);

  return (
    <div className="container">
      <div>
        <div
          className="mt-3 justify-content-center align-items-center mx-auto"
          style={{ width: "60vw", backgroundColor: "#ffffff" }}
        ></div>
        <h2 className="text-center text-white bg-success card mb-1">
          Gerenciamento de Jogadores
        </h2>
        <h6 className="card text-center text-white bg-success mb-1 pb-1">
          Informações do Jogador
        </h6>
        <div className="card-body text-center">
          <h5 className="card text-center text-white bg-dark mb-1 pb-1">
            {jogadorEditandoId ? "Atualizar Jogador" : "Cadastro de Jogadores"}
          </h5>
          <span className="card-text">
            <input
              className="mb-2 form-control"
              placeholder="Informe o Nome"
              value={nomeInput}
              onChange={(evento) => setNomeInput(evento.target.value)}
            />
            <input
              type="number"
              className="mb-2 form-control"
              placeholder="Informe a Idade"
              value={idadeInput}
              onChange={(evento) => setIdadeInput(evento.target.value)}
            />
            <input
              className="mb-2 form-control"
              placeholder="Informe o Time"
              value={timeInput}
              onChange={(evento) => setTimeInput(evento.target.value)}
            />
            <button
              className="btn btn-outline-success mb-4 mt-2"
              onClick={handleSubmitJogador}
            >
              {jogadorEditandoId ? "Atualizar" : "Cadastrar"}
            </button>
            {jogadorEditandoId && (
              <button
                className="btn btn-outline-secondary mb-4 mt-2 ms-2"
                onClick={limparFormulario}
              >
                Cancelar Edição
              </button>
            )}
          </span>

          <JogadorList
            jogadores={jogadorList}
            onDeleteJogador={handleDeleteJogador}
            onEditJogador={handleEditJogador}
          />
        </div>
        <h6 className="card text-center text-light bg-success py-1">
          &copy; DS - 2025
        </h6>
      </div>
    </div>
  );
}

export default App;