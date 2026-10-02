from datetime import datetime, timedelta

class PlayList:
    def __init__(self, id: int, nome: str, descricao: str):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def tempo_total(self, lista_itens: list, lista_musicas: list) -> timedelta:
        total = timedelta()
        # Mapeia músicas por id
        mapa_musicas = {m.get_id(): m for m in lista_musicas}
        for item in lista_itens:
            if item.get_id_playlist() == self.__id:
                musica = mapa_musicas.get(item.get_id_musica())
                if musica:
                    total += musica.get_duracao()
        return total

    def __str__(self):
        return f"Playlist ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"


class Musica:
    def __init__(self, id: int, titulo: str, artista: str, album: str, duracao: timedelta):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__duracao = duracao

    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_artista(self):
        return self.__artista

    def set_artista(self, artista: str):
        self.__artista = artista

    def get_album(self):
        return self.__album

    def set_album(self, album: str):
        self.__album = album

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao: timedelta):
        self.__duracao = duracao

    def __str__(self):
        return f"Música ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} | Duração: {self.__duracao}"


class PlayListItem:
    def __init__(self, id: int, id_playlist: int, id_musica: int, data_inclusao: datetime, sequencia: int):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__data_inclusao = data_inclusao
        self.__sequencia = sequencia

    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_id_playlist(self):
        return self.__id_playlist

    def set_id_playlist(self, id_playlist: int):
        self.__id_playlist = id_playlist

    def get_id_musica(self):
        return self.__id_musica

    def set_id_musica(self, id_musica: int):
        self.__id_musica = id_musica

    def get_data_inclusao(self):
        return self.__data_inclusao

    def set_data_inclusao(self, data_inclusao: datetime):
        self.__data_inclusao = data_inclusao

    def get_sequencia(self):
        return self.__sequencia

    def set_sequencia(self, sequencia: int):
        self.__sequencia = sequencia

    def __str__(self):
        dt_str = self.__data_inclusao.strftime("%d/%m/%Y %H:%M")
        return f"Item ID: {self.__id} | Playlist ID: {self.__id_playlist} | Música ID: {self.__id_musica} | Ordem: {self.__sequencia} | Inserido em: {dt_str}"


class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []

    def menu(self) -> int:
        print("\n--- MENU PLAYLIST APP ---")
        print("1 - Gerenciar Playlists (Inserir / Listar / Excluir)")
        print("2 - Gerenciar Músicas (Inserir / Listar / Excluir)")
        print("3 - Adicionar Música à Playlist")
        print("4 - Listar Músicas de uma Playlist")
        print("0 - Sair")
        try:
            return int(input("Opção: "))
        except ValueError:
            return -1

    def cadastrar_playlist(self):
        id_p = int(input("ID da Playlist: "))
        nome = input("Nome: ")
        desc = input("Descrição: ")
        self.playlists.append(PlayList(id_p, nome, desc))
        print("Playlist criada!")

    def cadastrar_musica(self):
        id_m = int(input("ID da Música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        segundos = int(input("Duração em segundos: "))
        self.musicas.append(Musica(id_m, titulo, artista, album, timedelta(seconds=segundos)))
        print("Música criada!")

    def adicionar_musica_playlist(self):
        id_i = int(input("ID do Item: "))
        id_p = int(input("ID da Playlist: "))
        id_m = int(input("ID da Música: "))
        seq = int(input("Sequência/Ordem na playlist: "))
        item = PlayListItem(id_i, id_p, id_m, datetime.now(), seq)
        self.itens.append(item)
        print("Música adicionada à playlist!")

    def listar_conteudo_playlist(self):
        id_p = int(input("ID da Playlist: "))
        pl = next((p for p in self.playlists if p.get_id() == id_p), None)
        if not pl:
            print("Playlist não encontrada.")
            return

        print(pl)
        tempo = pl.tempo_total(self.itens, self.musicas)
        print(f"Tempo Total da Playlist: {tempo}")
        print("Músicas:")
        itens_pl = [i for i in self.itens if i.get_id_playlist() == id_p]
        itens_pl.sort(key=lambda x: x.get_sequencia())
        for item in itens_pl:
            musica = next((m for m in self.musicas if m.get_id() == item.get_id_musica()), None)
            if musica:
                print(f"  [{item.get_sequencia()}] {musica.get_titulo()} - {musica.get_artista()} ({musica.get_duracao()})")

    def main(self):
        op = -1
        while op != 0:
            op = self.menu()
            if op == 1:
                self.cadastrar_playlist()
            elif op == 2:
                self.cadastrar_musica()
            elif op == 3:
                self.adicionar_musica_playlist()
            elif op == 4:
                self.listar_conteudo_playlist()
            elif op == 0:
                print("Saindo...")

if __name__ == "__main__":
    ui = UI()
    ui.main()