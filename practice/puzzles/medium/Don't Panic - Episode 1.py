
def resolve_board():
    for floor in range(nb_floors):
        if entrance_of[floor] > elevator_of[floor] and entry_direction_of[floor] == 1:
            blocking_position_of[floor] = entrance_of[floor] + 1
            entry_direction_of[floor+1] = -1
        elif entrance_of[floor] < elevator_of[floor] and entry_direction_of[floor] == -1:
            blocking_position_of[floor] = entrance_of[floor] - 1
            entry_direction_of[floor+1] = 1
        else:
            blocking_position_of[floor] = -1
            entry_direction_of[floor+1] = entry_direction_of[floor]
    return


# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for
                                                                                                             i in
                                                                                                             input().split()]
elevator_of, entrance_of, blocking_position_of, entry_direction_of = {}, {}, {}, {0:1}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator_of[elevator_floor] = elevator_pos
    entrance_of[elevator_floor + 1] = elevator_pos

# game loop
first = True
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    if 0 not in blocking_position_of and clone_pos >= 0:
        entrance_of[0] = clone_pos
        resolve_board()

    if clone_pos == blocking_position_of(clone_floor):
        print("BLOCK")
    else:
        print("WAIT")
