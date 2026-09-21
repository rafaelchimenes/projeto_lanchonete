class Cliente:

    ##Construtor + Atributos 
    def __init__(self, nome,cpf, tel, email, endereco):
        self.nome=nome
        self.cpf=cpf
        self.__telefone=tel #privado
        self.email=email
        self.endereco=endereco

    ##Encapsulamento (analisar se precisa)
    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, tel):
        self.__telefone=tel

    ##Metodos - ações
    def imprimeFicha(self):
        print(f"\n------------------------"
              f"\nNome: {self.nome}"
              f"\nCPF: {self.cpf}"
              f"\nTelefone: {self.__telefone}"
              f"\nE-mail: {self.email}"
              f"\nEndereço: {self.endereco}"
              f"\n------------------------"
              )
    