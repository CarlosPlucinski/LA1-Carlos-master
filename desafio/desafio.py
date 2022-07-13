def Cadastrar_Alunos():
  matricula = input('Matrícula: ')
  nome = input('Artista: ')
  
 
  
def Editar():
  d = int(input('Informe o ID da música a ser deletada: '))
 

def Cadastrar_Notas():
  for i in cursor.fetchall():
    print(i)

def Listar():
  cursor.execute("SELECT * FROM musica")
  for i in cursor.fetchall():
    print(i)

from time import sleep
menu = 0
while menu != 5:
  sleep(1)
  print('-'*50)
  print('{:^50}'.format(' MENU PRINCIPAL '))
  print('-'*50)
  print('\nO que deseja fazer?\n')
  print('''  [1] Cadastrar Aluno
  [2] Editar Informações do Aluno
  [3] Cadastrar notas de um Aluno
  [4] Listar Alunos
  [4] Sair do Programa''')
  menu = int(input('\nInforme a opção desejada: '))
  if menu == 1:
    print('-'*50)
    print('{:^50}'.format(' CADASTRAR ALUNO '))
    print('-'*50, '\n')
    Cadastrar_Alunos()
    print()
  elif menu == 2:
    print('-'*50)
    print('{:^50}'.format(' EDITAR INFORMAÇÕES '))
    print('-'*50,'\n')
    Editar()
    print()
    print()
  elif menu == 3:
    print('-'*50)
    print('{:^50}'.format(' CADASTRAR NOTAS '))
    print('-'*50,'\n')
    Cadastrar_Notas()
    print()
  elif menu == 4:
    print('-'*50)
    print('{:^50}'.format(' LISTAR ALUNOS '))
    print('-'*50,'\n')
    Listar()
    print()

  elif menu == 5:
    print('Finalizando...')
    sleep(2)
  else:
    print('Opção Inválida!')
print('Fim do Programa!')
