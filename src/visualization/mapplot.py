import matplotlib.pyplot as plt
import geopandas as gpd
from src.utils.logger import viz_logger

class JeddahMapVisualizer:
    def __init__(self, street_network, stations, hospitals):
        self.street_network = street_network
        self.stations = stations
        self.hospitals = hospitals
        
    def plot_base_map(self):
        viz_logger.info("Plotting base map of Jeddah")
        fig, ax = plt.subplots(figsize=(15, 15))
        self.street_network.plot(ax=ax, color='gray', linewidth=0.5)
        return fig, ax
    
    def add_stations(self, ax):
        viz_logger.info("Adding ambulance stations to map")
        self.stations.plot(ax=ax, color='blue', markersize=50, marker='^', label='Ambulance Stations')
        
    def add_hospitals(self, ax):
        viz_logger.info("Adding hospitals to map")
        self.hospitals.plot(ax=ax, color='red', markersize=50, marker='H', label='Hospitals')
        
    def add_response_times(self, ax, response_times):
        viz_logger.info("Adding response time heatmap to map")
        # Logic to create a heatmap of response times
        pass
    
    def save_map(self, fig, filename):
        viz_logger.info(f"Saving map to {filename}")
        fig.savefig(filename)
        plt.close(fig)
        
    def create_full_visualization(self, response_times, filename):
        fig, ax = self.plot_base_map()
        self.add_stations(ax)
        self.add_hospitals(ax)
        self.add_response_times(ax, response_times)
        ax.legend()
        self.save_map(fig, filename)
        viz_logger.info("Full visualization created and saved")