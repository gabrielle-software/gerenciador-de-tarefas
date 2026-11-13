
import json
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "tarefas.json"


def carregar_tarefas():
    if ARQUIVO.exists():
        try:
            return json.loads(ARQUIVO.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Erro ao carregar as tarefas.")
    return []


def salvar_tarefas(tarefas):
    ARQUIVO.write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )


def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n--- MINHAS TAREFAS ---")
    for numero, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f'{numero}. [{status}] {tarefa["descricao"]}')


def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)

        elif opcao == "2":
            descricao = input("Descrição da tarefa: ").strip()
            if descricao:
                tarefas.append({
                    "descricao": descricao,
                    "concluida": False
                })
                salvar_tarefas(tarefas)
                print("Tarefa adicionada!")
            else:
                print("A descrição não pode ficar vazia.")

        elif opcao == "3":
            listar_tarefas(tarefas)
            if tarefas:
                try:
                    numero = int(input("Número da tarefa concluída: "))
                    if 1 <= numero <= len(tarefas):
                        tarefas[numero - 1]["concluida"] = True
                        salvar_tarefas(tarefas)
                        print("Tarefa concluída!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")

        elif opcao == "4":
            listar_tarefas(tarefas)
            if tarefas:
                try:
                    numero = int(input("Número da tarefa a excluir: "))
                    if 1 <= numero <= len(tarefas):
                        tarefas.pop(numero - 1)
                        salvar_tarefas(tarefas)
                        print("Tarefa excluída!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
