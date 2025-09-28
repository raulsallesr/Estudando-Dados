tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(bord):
    for linha in bord:
        print(f"| {linha[0]} | {linha[1]} | {linha[2]} |")
        print()

def jogada(jogador):
    # Mostre uma mensagem dizendo de quem é a vez (Jogador 1 para X, Jogador 2 para O)
    
    # Peça para o jogador digitar uma posição de 1 a 9 (validar se o valor é um número e está no intervalo correto)
    # Converta essa posição para índices linha e coluna do tabuleiro
    # Verifique se a posição escolhida está vazia (" ")
    # Se estiver vazia, coloque o símbolo do jogador nessa posição e saia do loop
    # Se não estiver, avise que a posição está ocupada e peça para tentar de novo
    pass  # Substitua por seu código

def checar_vitoria(tabuleiro):
    # Verifique as 3 linhas: se alguma linha tem 3 símbolos iguais (e não vazios), retorne esse símbolo
    # Verifique as 3 colunas: se alguma coluna tem 3 símbolos iguais (e não vazios), retorne esse símbolo
    # Verifique as duas diagonais da mesma forma
    # Se nenhuma condição de vitória for encontrada, retorne None
    pass  # Substitua por seu código

def checar_empate(tabuleiro):
    # Verifique se todas as posições do tabuleiro estão preenchidas (sem espaços vazios)
    # Se todas estiverem preenchidas, retorne True (empate)
    # Caso contrário, retorne False (ainda tem jogadas possíveis)
    pass  # Substitua por seu código

while True:
    # Mostre o tabuleiro
    # Faça a jogada do jogador X
    # Verifique se alguém ganhou
    # Se sim, mostre o tabuleiro, avise quem venceu e pare o jogo
    # Verifique se deu empate
    # Se sim, mostre o tabuleiro, avise o empate e pare o jogo

    # Mostre o tabuleiro
    # Faça a jogada do jogador O
    # Verifique se alguém ganhou
    # Se sim, mostre o tabuleiro, avise quem venceu e pare o jogo
    # Verifique se deu empate
    # Se sim, mostre o tabuleiro, avise o empate e pare o jogo
    pass  # Substitua por seu código
