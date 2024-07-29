#(OldVehicleLibrary)
class OldVehicleStorage: #AQUI TEMOS A ANTIGA CLASSE (CLASSE LEGADA)
    def storeVehicleData(self, data: str):
        print(f"Dados do veiculo no formato antigo: {data}")

#(NewVehicleLibrary)
class IVehicleStorage: #AQUI TEMOS A NOVA CLASSE
    def saveVehicleData(self, vehicle: 'Vehicle'):
        raise NotImplementedError("Metodo a ser implementado por subclasses")

class Vehicle: #AQUI TEMOS OS DADOS DO VEICULO A SER ARMAZENADOS ID, MODEL, YEAR E SEUS RETORNOS
    def __init__(self, id: str, model: str, year: int):
        self.id = id
        self.model = model
        self.year = year

    def get_id(self):
        return self.id

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def __str__(self): #AQUI TEMOS A IMPRESSAO 
        return f"Vehicle(id={self.id}, model={self.model}, year={self.year})"

class VehicleStorageAdapter(IVehicleStorage):
    def __init__(self, old_storage: OldVehicleStorage):
        self.old_storage = old_storage

    def saveVehicleData(self, vehicle: Vehicle):
        data = f"ID: {vehicle.get_id()}, Model: {vehicle.get_model()}, Year: {vehicle.get_year()}"
        self.old_storage.storeVehicleData(data) 

def main():
    vehicle = Vehicle(id="3355", model="Truck", year=2020)
    print(f"Criando o veiculo: {vehicle}")

    old_storage = OldVehicleStorage()
    adapter = VehicleStorageAdapter(old_storage)

    adapter.saveVehicleData(vehicle) 

if __name__ == "__main__":
    main()
