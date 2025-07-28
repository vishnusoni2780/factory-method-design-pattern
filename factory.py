from modes import (
    air,
    road,
    sea
)

class Factory:
    def __init__(self):
        print("[+] Requested Factory!")
    
    _map = {
        "air": air.Air,
        "road": road.Road,
        "sea": sea.Sea,
    }
    
    @classmethod
    def get_normalizer(self, tranport_type: str):
        return self._map.get(tranport_type.lower())

    def decide_transport_mode(self, tranport_type):
        if tranport_type == 'air':
            return air.Air()
        elif tranport_type == 'road':
            return road.Road()
        elif tranport_type == 'sea':
            return sea.Sea()
        else:
            return None
