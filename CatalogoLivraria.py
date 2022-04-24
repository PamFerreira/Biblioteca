# Entrada de dados de livro à catálogo de livraria.
class Livro:
    titulo = ''
    genero = ''
    subgenero = ''
    editora = ''
    copias = ''
    valor = ''
    
Livros = {}

lvr = Livro()
print('--- Adição de mais um livro ---')
lvr.titulo = input('Digite o título do livro: ')
lvr.genero = input('Digite o gênero do livro: ')
lvr.subgenero = input('Digite o subgênero do livro: ')
lvr.editora = input('Digite a editora do livro: ')
lvr.copias = input('Digite o número de cópias do livro: ')
lvr.valor = input('Digite o valor do livro: ')

item = lvr.titulo
if item not in Livros: 
    Livros[item] = [] 
    Livros[item].append(lvr) 
    
for lvr in sorted(Livros[item], key=lambda c : c.titulo):  
    print('Título: {}\tGênero: {}\tSubgênero: {}\tEditora: {}\tCópias: {}\tValor: {}'.format(lvr.titulo, lvr.genero, lvr.subgenero, lvr.editora, lvr.copias, lvr.valor))
    print('')
    
for lvr in sorted(Livros[item], key=lambda c : c.genero): 
    print('Gênero: {}\tSubgênero: {}\tTítulo: {}'.format(lvr.genero, lvr.subgenero, lvr.titulo))
