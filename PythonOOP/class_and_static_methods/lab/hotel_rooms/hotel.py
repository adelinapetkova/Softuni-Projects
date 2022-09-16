from class_and_static_methods.lab.hotel_rooms.room import Room


class Hotel:
    def __init__(self, name:str):
        self.name = name
        self.rooms=[]
        self.guests=0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room:Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number==room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number==room_number:
                room.free_room()

    def status(self):
        for r in self.rooms:
            if r.is_taken:
                self.guests+=r.guests
        free=[str(r.number) for r in self.rooms if not r.is_taken]
        taken=[str(r.number) for r in self.rooms if r.is_taken]

        return \
            f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {", ".join(free)}
Taken rooms: {", ".join(taken)}"""
