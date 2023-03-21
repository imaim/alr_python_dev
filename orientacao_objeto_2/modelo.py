class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def __str__(self):
        return f"{self._nome} - {self._ano} : {self._likes} Likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self._duracao} min - {self.get_ano} : {self.get_likes} Likes"

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

    def __str__(self):
        return f"{self.nome} - {self._temporadas} Temporadas - {self.get_ano} : {self.get_likes} Likes"

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
    def get_temporadas(self):
        return self._temporadas

    def dar_like(self):
        self._likes += 1


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # methodo mágico de sequencia
    def __getitem__(self, item):
        return self._programas[item]

    # methodo mágico de len(), importa um comportamento do modulo len()
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


vingadores = Filme("vingadores guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)
# print(f"{vingadores.nome.title()} - {vingadores.get_duracao} : {vingadores.get_likes}")
# print(f"{atlanta.nome.title()} - {atlanta.get_temporadas} : {atlanta.get_likes}")
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
vingadores.dar_like()
filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"O tamanho da Playlist é {len(playlist_fim_de_semana)}")
# print(demolidor in playlist_fim_de_semana)
for programa in playlist_fim_de_semana:
    print(programa)
