from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, data: datetime, distancia: float, tempo: timedelta):
        self.__id = id
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo

    # Getters e Setters
    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data: datetime):
        self.__data = data

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia: float):
        self.__distancia = distancia

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, tempo: timedelta):
        self.__tempo = tempo

    # Método Pace (Tempo médio por quilômetro)
    def pace(self) -> timedelta:
        if self.__distancia <= 0:
            return timedelta(0)
        segundos_por_km = self.__tempo.total_seconds() / self.__distancia
        return timedelta(seconds=segundos_por_km)

    def __str__(self):
        data_str = self.__data.strftime("%d/%m/%Y")
        pace_td = self.pace()
        minutos = int(pace_td.total_seconds() // 60)
        segundos = int(pace_td.total_seconds() % 60)
        return (f"ID: {self.__id} | Data: {data_str} | Distância: {self.__distancia:.2f} km | "
                f"Tempo: {self.__tempo} | Pace: {minutos:02d}:{segundos:02d} min/km")


class TreinoUI:
    def __init__(self):
        self.treinos = []

    def menu(self) -> int:
        print("\n--- MENU TREINOS ---")
        print("1 - Inserir novo treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar treino por ID")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Treino mais rápido (menor pace)")
        print("0 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def inserir(self):
        try:
            id_t = int(input("ID: "))
            data_str = input("Data (DD/MM/AAAA): ")
            data = datetime.strptime(data_str, "%d/%m/%Y")
            distancia = float(input("Distância (km): "))
            minutos = int(input("Tempo total (em minutos): "))
            tempo = timedelta(minutes=minutos)

            treino = Treino(id_t, data, distancia, tempo)
            self.treinos.append(treino)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir treino: {e}")

    def listar(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return
        for t in self.treinos:
            print(t)

    def listar_id(self):
        try:
            id_t = int(input("Informe o ID: "))
            for t in self.treinos:
                if t.get_id() == id_t:
                    print(t)
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido.")

    def atualizar(self):
        try:
            id_t = int(input("Informe o ID do treino a atualizar: "))
            for t in self.treinos:
                if t.get_id() == id_t:
                    data_str = input("Nova Data (DD/MM/AAAA): ")
                    t.set_data(datetime.strptime(data_str, "%d/%m/%Y"))
                    t.set_distancia(float(input("Nova Distância (km): ")))
                    minutos = int(input("Novo Tempo total (minutos): "))
                    t.set_tempo(timedelta(minutes=minutos))
                    print("Treino atualizado com sucesso!")
                    return
            print("Treino não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar: {e}")

    def excluir(self):
        try:
            id_t = int(input("Informe o ID do treino a excluir: "))
            for t in self.treinos:
                if t.get_id() == id_t:
                    self.treinos.remove(t)
                    print("Treino excluído com sucesso!")
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido.")

    def mais_rapido(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return
        # Menor pace significa maior velocidade média
        treino_rapido = min(self.treinos, key=lambda t: t.pace())
        print("Treino mais rápido:")
        print(treino_rapido)

    def main(self):
        op = -1
        while op != 0:
            op = self.menu()
            if op == 1:
                self.inserir()
            elif op == 2:
                self.listar()
            elif op == 3:
                self.listar_id()
            elif op == 4:
                self.atualizar()
            elif op == 5:
                self.excluir()
            elif op == 6:
                self.mais_rapido()
            elif op == 0:
                print("Saindo...")
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    ui = TreinoUI()
    ui.main()