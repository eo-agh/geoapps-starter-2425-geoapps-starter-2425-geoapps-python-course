from geoapps.zajecia03.fleet.ambulance import Ambulance
from geoapps.zajecia03.operations.incident_queue import IncidentQueue
# from .fleet import *
# from .operations import *


class Management(Ambulance, IncidentQueue):
    def __init__(self, incidents, ambulances):
        self.incidents = incidents
        self.ambulances = ambulances

    def assign_ambulances(self):
        for incident in self.incidents:
            if incident.status != "pending":
                continue
            available_ambulances = [a for a in self.ambulances if a.isavailable()]
            if available_ambulances:
                best_ambulance = min(
                    available_ambulances, key=lambda a: a.distance_to(incident.location)
                )
                if best_ambulance.assign_to_incident(incident):
                    incident.status = "assigned"
                    print(
                        f"Assigned Ambulance {best_ambulance.id} to Incident {incident.id}"
                    )
