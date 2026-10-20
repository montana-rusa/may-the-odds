class Arena:
    def __init__(self) -> None:
        self.tribute_map = [ 
         [], [], [], [], [],
         [], [], [], [], [],
         [], [], [], [], [],
         [], [], [], [], [],
         [], [], [], [], [],
        ]

    @property
    def tribute_map(self) -> list[list]:
        return self._tribute_map

    @tribute_map.setter
    def tribute_map(self, value: list[list]) -> None:
        self._tribute_map = value

    

