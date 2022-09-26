from exam_preparation.exam_22_08.project.rooms.alone_old import AloneOld
from exam_preparation.exam_22_08.project.rooms.alone_young import AloneYoung
from exam_preparation.exam_22_08.project.rooms.old_couple import OldCouple
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()


def test_one():
    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)

    alone_old = AloneOld("AloneOld", 200.00)
    alone_young = AloneYoung("AloneYoung", 300.00)
    old_couple = OldCouple("OldCouple", 200.00, 300.00)
    young_couple = YoungCouple("Johnsons", 150, 205)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(alone_old)
    everland.add_room(alone_young)
    everland.add_room(old_couple)
    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()