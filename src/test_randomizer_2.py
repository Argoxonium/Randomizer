from modules.randomizer import *

equipment_data = pd.DataFrame({
    'Owner': ['John', 'Jane', 'John', 'bob'],
    'Room': ['Lab1', 'Lab2', 'Lab1','Lab1'],
    'Equipment': ['Hood 2', 'Glovebox 1', 'Glovebox 1','Hood 3']
})

event = RandomReviewers(equipment_data, None)

try:
    # Assume `self.equipment = equipment_data` if not explicitly passed
    result = event.room_check(
        reviewer="Alice",
        review_number=2,
        owner="John",
        room="Lab1",
        equipment_df=equipment_data
    )
    print(result)
except ValueError as e:
    print(e)
