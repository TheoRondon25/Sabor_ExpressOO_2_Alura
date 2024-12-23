from exercicios import Livro

livro_biblioteca = Livro('Livro da biblioteca', 'Neymar', 2018)

Livro.livros.append(livro_biblioteca)

# Livro.emprestar(livro_biblioteca)
# print(livro_biblioteca)

# DISPONIVEL DEVE ESTAR TRUE PARA QUE SEJA EXIBIDO
ano_especifico = 1997
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")


