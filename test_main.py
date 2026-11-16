import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class TestGerenciadorDeTarefas(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.arquivo_original = main.ARQUIVO
        main.ARQUIVO = Path(self.temp_dir.name) / "tarefas.json"

    def tearDown(self):
        main.ARQUIVO = self.arquivo_original
        self.temp_dir.cleanup()

    def test_carregar_tarefas_sem_arquivo_retorna_lista_vazia(self):
        self.assertEqual(main.carregar_tarefas(), [])

    def test_carregar_tarefas_com_json_valido(self):
        tarefas = [{"descricao": "Estudar Python", "concluida": False}]
        main.ARQUIVO.write_text(json.dumps(tarefas), encoding="utf-8")
        self.assertEqual(main.carregar_tarefas(), tarefas)

    def test_carregar_tarefas_com_json_invalido_retorna_lista_vazia(self):
        main.ARQUIVO.write_text("{json inválido", encoding="utf-8")
        with patch("builtins.print") as imprimir:
            resultado = main.carregar_tarefas()
        self.assertEqual(resultado, [])
        imprimir.assert_called_once_with("Erro ao carregar as tarefas.")

    def test_salvar_tarefas_grava_json_corretamente(self):
        tarefas = [{"descricao": "Revisar portfólio", "concluida": True}]
        main.salvar_tarefas(tarefas)
        dados_gravados = json.loads(main.ARQUIVO.read_text(encoding="utf-8"))
        self.assertEqual(dados_gravados, tarefas)

    def test_listar_tarefas_vazias_informa_que_nao_ha_tarefas(self):
        with patch("builtins.print") as imprimir:
            main.listar_tarefas([])
        imprimir.assert_called_once_with("\nNenhuma tarefa cadastrada.")

    def test_listar_tarefas_exibe_status_e_descricao(self):
        tarefas = [
            {"descricao": "Estudar testes", "concluida": False},
            {"descricao": "Atualizar README", "concluida": True},
        ]
        with patch("builtins.print") as imprimir:
            main.listar_tarefas(tarefas)
        saida = "\n".join(str(chamada.args[0]) for chamada in imprimir.call_args_list)
        self.assertIn("[Pendente] Estudar testes", saida)
        self.assertIn("[Concluída] Atualizar README", saida)

    def test_fluxo_adicionar_concluir_e_excluir_tarefa(self):
        entradas = ["2", "Estudar Python", "3", "1", "4", "1", "0"]
        with patch("builtins.input", side_effect=entradas), patch("builtins.print"):
            main.main()
        self.assertEqual(main.carregar_tarefas(), [])


if __name__ == "__main__":
    unittest.main()
