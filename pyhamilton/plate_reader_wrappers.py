from .interface import BIOTEKGEN5_INITIALIZE, BIOTEKGEN5_DOOR

std_timeout = 10 # seconds

DOOR_ACTION_OPEN = True
DOOR_ACTION_CLOSE = False

def plate_reader_init(ham, simulate=False, timeout=std_timeout):
    return_field = ['step-return1']
    cmd = ham.send_command(BIOTEKGEN5_INITIALIZE, Simulate=simulate)
    response = ham.wait_on_response(cmd, raise_first_exception=True, timeout=timeout, return_data=return_field)
    result = response.return_data[0]
    return result

def plate_reader_door_open(ham, timeout=std_timeout):
    return_field = ['step-return1']
    cmd = ham.send_command(BIOTEKGEN5_DOOR, DoorAction=DOOR_ACTION_OPEN)
    response = ham.wait_on_response(cmd, raise_first_exception=True, timeout=timeout, return_data=return_field)
    result = response.return_data[0]
    return result

def plate_reader_door_close(ham, timeout=std_timeout):
    return_field = ['step-return1']
    cmd = ham.send_command(BIOTEKGEN5_DOOR, DoorAction=DOOR_ACTION_CLOSE)
    response = ham.wait_on_response(cmd, raise_first_exception=True, timeout=timeout, return_data=return_field)
    result = response.return_data[0]
    return result
