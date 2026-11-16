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
    try:
        ARQUIVO.write_text(
            json.dumps(tarefas, ensure_ascii=False, indent=4),
            encoding="utf-8"
        )
        return True
    except OSError:
        print("Erro ao salvar as tarefas.")
        return False


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
                novas_tarefas = tarefas + [{
                    "descricao": descricao,
                    "concluida": False
                }]
                if salvar_tarefas(novas_tarefas):
                    tarefas = novas_tarefas
                    print("Tarefa adicionada!")
            else:
                print("A descrição não pode ficar vazia.")

        elif opcao == "3":
            listar_tarefas(tarefas)
            if tarefas:
                try:
                    numero = int(input("Número da tarefa concluída: "))
                    if 1 <= numero <= len(tarefas):
                        novas_tarefas = [dict(tarefa) for tarefa in tarefas]
                        novas_tarefas[numero - 1]["concluida"] = True
                        if salvar_tarefas(novas_tarefas):
                            tarefas = novas_tarefas
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
                        novas_tarefas = tarefas.copy()
                        novas_tarefas.pop(numero - 1)
                        if salvar_tarefas(novas_tarefas):
                            tarefas = novas_tarefas
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
