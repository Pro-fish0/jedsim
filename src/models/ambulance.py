from src.utils.logger import model_logger

class Ambulance:
    def __init__(self, id, station):
        self.id = id
        self.station = station
        self.status = "available"
        self.current_location = station.location
        model_logger.info(f"Ambulance {id} initialized at station {station.id}")

    def dispatch(self, incident):
        self.status = "dispatched"
        model_logger.info(f"Ambulance {self.id} dispatched to incident {incident.id}")

    def arrive(self, incident):
        self.status = "on_scene"
        self.current_location = incident.location
        model_logger.info(f"Ambulance {self.id} arrived at incident {incident.id}")

    def transport(self, hospital):
        self.status = "transporting"
        model_logger.info(f"Ambulance {self.id} transporting to hospital {hospital.id}")

    def return_to_station(self):
        self.status = "returning"
        model_logger.info(f"Ambulance {self.id} returning to station {self.station.id}")

    def arrive_at_station(self):
        self.status = "available"
        self.current_location = self.station.location
        model_logger.info(f"Ambulance {self.id} arrived at station {self.station.id}")