class PlataformaDeVideo:
    def __init__(self):
        # DICIONÁRIO
        self.observadores = {}

    def adicionar_observador(self, usuario, genero): 
        if genero not in self.observadores:
            self.observadores[genero] = []
        if usuario not in self.observadores[genero]:
            self.observadores[genero].append(usuario)
            print(f"{usuario.nome} se inscreveu para notificações do gênero {genero}.")
        else:
            print(f"{usuario.nome} já está inscrito para notificações do gênero {genero}.")

    def remover_observador(self, usuario, genero):
        if genero in self.observadores and usuario in self.observadores[genero]:
            self.observadores[genero].remove(usuario)
            print(f"{usuario.nome} cancelou a inscrição para notificações do gênero {genero}.")
        else:
            print(f"{usuario.nome} não está inscrito para notificações do gênero {genero}.")

    def notificar_observadores(self, genero, conteudo):
        if genero in self.observadores:
            for observador in self.observadores[genero]:
                observador.atualizar(genero, conteudo)

#OBSERVER
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.generos = []

    def atualizar(self, genero, conteudo):
        print(f"Notificação para {self.nome}: Novo conteúdo '{conteudo.nome}' disponível no gênero {genero}.")

class Conteudo:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

if __name__ == "__main__":
    plataforma = PlataformaDeVideo()

#DEFIÇÃO NÚMERO DE USUÁRIOS 
    usuario1 = Usuario("João Vitor")
    usuario2 = Usuario("Vútão Mendes")
    usuario3 = Usuario("Sara")
    usuario4 = Usuario("Leon")
    usuario5 = Usuario("Bruce")
    usuario6 = Usuario("Mickey")
    usuario7 = Usuario("Belinha")

    print('-------------------------------------------------------------------------------------------------')
#ADICIONANDO USUÁRIO A SEU GENERO DE FILME
    plataforma.adicionar_observador(usuario1, "ação")
    plataforma.adicionar_observador(usuario2, "comédia")
    plataforma.adicionar_observador(usuario3, "terror")
    plataforma.adicionar_observador(usuario4, "ação")
    plataforma.adicionar_observador(usuario5, "ficção científica")
    plataforma.adicionar_observador(usuario6, "drama")
    plataforma.adicionar_observador(usuario7, "ação")
    plataforma.adicionar_observador(usuario7, "comédia")

    print('-------------------------------------------------------------------------------------------------')
#TESTES DE ADICIONAR USUARIO A UM FILME JA ADICIONADO ANTERIORMENTE, TESTE DE CANCELAMENTO DE UM FILME E TESTE DE CANCELAR SEM  INSCRIÇÃO
#O PADRÃO OBSERVER É MUITO ÚTIL QUANDO TEMOS A NECESSIDADE DE NOTIFICAR MULTIPLOS OBJETOS SOBRE MUDANÇA DE ESTADO DE OUTRO OBJETO

    #JÁ INSCRITO
    plataforma.adicionar_observador(usuario1, "ação")

    #CANCELAR INSCRIÇÃO
    plataforma.remover_observador(usuario7, "ação")

    #CANCELANDO SEM ESTAR INSCRITO
    plataforma.remover_observador(usuario7, "terror")

#ADICIONANDO NOVOS FILMES/EPISODIOS 
    novo_filme1 = Conteudo("Interstellar", "ficção científica")
    novo_filme2 = Conteudo("Parasita", "drama")
    novo_episodio1 = Conteudo("Breaking Bad", "ação")
    novo_episodio2 = Conteudo("Gente Grande", "comédia")
    novo_filme3 = Conteudo("Invocação do Mal", "terror")

    print('-------------------------------------------------------------------------------------------------')
#NOTIFICAÇÕES DOS FILMES PARA OS USUÁRIOS 
    plataforma.notificar_observadores(novo_filme1.genero, novo_filme1)  
    plataforma.notificar_observadores(novo_filme2.genero, novo_filme2)  
    plataforma.notificar_observadores(novo_episodio1.genero, novo_episodio1)  
    plataforma.notificar_observadores(novo_episodio2.genero, novo_episodio2)  
    plataforma.notificar_observadores(novo_filme3.genero, novo_filme3)  

    print('-------------------------------------------------------------------------------------------------')

