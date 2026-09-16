from Pedido import Pedido

#criar um objeto - representar um elemento - dar valores 
novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
                     ["X-Salada", "X-bacon"], "Pix")

# ##### o que eu posso fazer com o Objeto? ####
# #acessar um atributo
# print(novoPedido.num)
# print(novoPedido.status)
# #alterar os dados de um atributo
# novoPedido.cliente="Rafael Martins"
# print(novoPedido.cliente)

# #chamando os metodos
# novoPedido.imprimir()
# novoPedido.atualizar_pedido("Em preparação")

#acessar o id - private
#novoPedido.__num=2
#print(novoPedido.__num) #acessar
#novoPedido.imprimir()
print(novoPedido.getNum())
novoPedido.setNum(2)
print(novoPedido.getNum())

novoPedido.setIten("X-Calabresa")
novoPedido.imprimir()