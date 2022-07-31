from app.machine import Machine
from app.queues.at_tree import AtTreeState
from app.queues.dirty import DirtyState
from app.queues.clean import CleanState
from app.operators.pick import PickOperator
from app.operators.clear import ClearOperator


def main():

    # Creating States
    initial_state = AtTreeState()
    intermediate_state = DirtyState()
    final_state = CleanState()

    # Creating Operators
    pick_operator = PickOperator(from_queue=initial_state, to_queue= intermediate_state, quantity=3)
    clear_operator = ClearOperator(from_queue=intermediate_state, to_queue= final_state, quantity=2)

    # Creating Machine
    machine = Machine(operators=[pick_operator, clear_operator])

    # Running
    machine.feed(50)
    machine.run()

if __name__ == "__main__":

    main()
