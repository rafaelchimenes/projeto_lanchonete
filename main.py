import os
from Pedido import Pedido
from Cliente import Cliente

os.system("cls")
#criar um objeto - representar um elemento - dar valores 
#novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
#                    ["X-Salada", "X-bacon"], "Pix")

###### o que eu posso fazer com o Objeto? ####
##acessar um atributo
# print(novoPedido.cliente)
# print(novoPedido.status)

##alterar os dados de um atributo
# novoPedido.cliente="Rafael Martins"
# print(novoPedido.cliente)

###chamando os metodos
# novoPedido.imprimir()
# novoPedido.atualizar_pedido("Em preparação")

#acessar o id - private
#novoPedido.__num=2 #ERRO PO SER PRIVADO
#print(novoPedido.__num) #acessar - ERRO PO SER PRIVADO
# print(novoPedido.getNum())
# novoPedido.setNum(2)
# print(novoPedido.getNum())

# novoPedido.setIten("X-Calabresa")
# novoPedido.imprimir()

#cadastro do cliente
novoCliente = Cliente(endereco="Rua Vital Brasil", email="joao@gmail.com",
                      cpf="033888665598", nome="João Desenvolvedor", tel="679988-6677")
novoCliente.imprimeFicha()

#novo pedido
novoPedido = Pedido(1, "14/09/2026", "21:10", novoCliente,
                    ["X-Salada", "X-bacon"], "Pix")
novoPedido.imprimirPedido()