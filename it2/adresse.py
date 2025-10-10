class Adresse:
    def __init__(self, gate, by):
        self._gate = gate
        self._by = by
    def __str__(self):
        return f"{self._gate}, {self._by}"
