import sys

agenda = {}
id = 1

def menu():
  print "\nSELECIONE UMA OPÇÃO ABAIXO"
  print "1. Cadastrar contato"
  print "2. Exibir contato"
  print "3. Editar contato"
  print "4. Remover contato"
  print "0. Sair"
  opcao = int(raw_input())
  
  if opcao == 1:
    cadastra()
  elif opcao == 2:
    exibe()
  elif opcao == 3:
    edita()
  elif opcao == 4:
    remove()
  elif opcao == 0:
    sai()
  else:
    print "Opção inválida"
    menu()

def cadastra():
  contato = {}
  global id 
  
  nome = raw_input("Nome: ")
  telefone = raw_input("Telefone: ")
  email = raw_input("Email: ")
  
  contato["Nome"] = nome 
  contato["Telefone"] = telefone
  contato["Email"] = email
  
  agenda[id] = contato
  id += 1
  print "\nContato inserido com sucesso!\n"
  menu()
  
def exibe():
  for id, contato in agenda.iteritems():
    print '\n' + str(id) + ':'
    for k, v in agenda[id].iteritems():
      print str(k) + ' -> ' + str(v)
    
  menu()

def edita():
  id_atual = int(raw_input("Digite o id do usuário que deseja alterar: "))
  chave = raw_input("Digite o campo que deseja alterar: ")
  valor = raw_input("Digite o novo valor: ")
  
  for k, v in agenda[id_atual].iteritems():
    if k == chave:
      agenda[id_atual][k] = valor
      break
  
  exibe()

def remove():
  id_atual = int(raw_input("Selecione o índice do contato que deseja remover: "))
  if id_atual <= id:
    del agenda[id_atual]
    print "\nContato removido com sucesso!"
    atualiza_indices()
  else:
    print "\nRemova um índice válido!\n"
    remove()
  
  exibe()
  menu()
  
def sai():
  print "Saindo..."
  sys.exit(0)
  
def atualiza_indices():
  global agenda
  novo_id = 1
  nova_agenda = {}
  for id, contato in agenda.iteritems():
    nova_agenda[novo_id] = contato
    novo_id += 1
    
  agenda = nova_agenda
  exibe()
  
menu()
