class DecorationRepository:
    decorations: list

    def __init__(self):
        self.decorations=[]

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        self.decorations.remove(decoration)

    def find_by_type(self, decoration_type: str):
        for d in self.decorations:
            if d.__DECORATION_TYPE==decoration_type:
                return d
        return None

