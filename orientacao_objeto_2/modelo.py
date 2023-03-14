class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def get_likes(self):
        return self._likes

    @property
    def get_ano(self):
        return self._ano

    @property
    def get_duracao(self):
        return self._duracao

    def dar_like(self):
        self._likes += 1


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def get_nome(self):
        return self._nome

    @get_nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def get_likes(self):
        return self._likes

    @property
    def get_ano(self):
        return self._ano

    @property
    def get_temporadas(self):
        return self._temporadas

    def dar_like(self):
        self._likes += 1


vingadores = Filme("vingadores guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
print(f"{vingadores.nome.title()} - {vingadores.get_duracao} : {vingadores.get_likes}")
vingadores.dar_like()
vingadores.dar_like()
print(f"{vingadores.nome.title()} - {vingadores.get_duracao} : {vingadores.get_likes}")

atlanta.nome = "Atllanta"
print(f"{atlanta.nome.title()} - {atlanta.get_duracao} : {atlanta.get_likes}")
