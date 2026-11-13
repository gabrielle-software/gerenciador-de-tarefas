
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import main


class TestGerenciadorDeTarefas(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.arquivo = Path(self.temp_dir.name) / "tarefas.json"

        self.patcher = patch.object(main, "ARQUIVO", self.arquivo)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_carregar_sem_arquivo(self):
        tarefas = main.carregar_tarefas()
        self.assertEqual(tarefas, [])

    def test_salvar_e_carregar_tarefas(self):
        tarefas = [
            {"descricao": "Estudar Python", "concluida": False}
        ]

        main.salvar_tarefas(tarefas)
        resultado = main.carregar_tarefas()

        self.assertEqual(resultado, tarefas)

    def test_carregar_json_invalido(self):
        self.arquivo.write_text("{ inválido", encoding="utf-8")

        tarefas = main.carregar_tarefas()

        self.assertEqual(tarefas, [])


    def test_adicionar_tarefa_pelo_menu(self):
        with patch("builtins.input", side_effect=["2", "Estudar SQL", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["descricao"], "Estudar SQL")

    def test_concluir_tarefa_pelo_menu(self):
        main.salvar_tarefas([
            {"descricao": "Estudar Python", "concluida": False}
        ])

        with patch("builtins.input", side_effect=["3", "1", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertTrue(tarefas[0]["concluida"])

    def test_excluir_tarefa_pelo_menu(self):
        main.salvar_tarefas([
            {"descricao": "Estudar GitHub", "concluida": False}
        ])

        with patch("builtins.input", side_effect=["4", "1", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertEqual(tarefas, [])

    def test_adicionar_tarefa_pelo_menu(self):
        with patch("builtins.input", side_effect=["2", "Estudar SQL", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["descricao"], "Estudar SQL")

    def test_concluir_tarefa_pelo_menu(self):
        main.salvar_tarefas([
            {"descricao": "Estudar Python", "concluida": False}
        ])

        with patch("builtins.input", side_effect=["3", "1", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertTrue(tarefas[0]["concluida"])

    def test_excluir_tarefa_pelo_menu(self):
        main.salvar_tarefas([
            {"descricao": "Estudar GitHub", "concluida": False}
        ])

        with patch("builtins.input", side_effect=["4", "1", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertEqual(tarefas, [])

    def test_adicionar_tarefa_pelo_menu(self):
        with patch("builtins.input", side_effect=["2", "Estudar SQL", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["descricao"], "Estudar SQL")

    def test_concluir_tarefa_pelo_menu(self):
        main.salvar_tarefas([
            {"descricao": "Estudar Python", "concluida": False}
        ])

        with patch("builtins.input", side_effect=["3", "1", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertTrue(tarefas[0]["concluida"])

    def test_excluir_tarefa_pelo_menu(self):
        main.salvar_tarefas([
            {"descricao": "Estudar GitHub", "concluida": False}
        ])

        with patch("builtins.input", side_effect=["4", "1", "0"]):
            main.main()

        tarefas = main.carregar_tarefas()
        self.assertEqual(tarefas, [])

if __name__ == "__main__":
    unittest.main()
