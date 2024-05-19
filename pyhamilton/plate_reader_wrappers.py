from .interface import BIOTEKGEN5_INITIALIZE, BIOTEKGEN5_DOOR, BIOTEKGEN5_READ_PLATE

std_timeout = 10 # seconds

DOOR_ACTION_OPEN = "Open"
DOOR_ACTION_CLOSE = "Close"

def plate_reader_init(ham, timeout=std_timeout):
    return_field = ['step-return1']
    cmd = ham.send_command(BIOTEKGEN5_INITIALIZE)
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

def plate_reader_read_plate(ham, experiment_path, export_path, timeout=300):
    import os
    if os.path.exists(export_path):
        print(f'WARNING(plate_reader_plate_data_export): path "{export_path}" exists and will be overwritten.')
        os.remove(export_path)
    return_field = ['step-return1']
    cmd = ham.send_command(BIOTEKGEN5_READ_PLATE, ExperimentPath=experiment_path, ExportPath=export_path)
    response = ham.wait_on_response(cmd, raise_first_exception=True, timeout=timeout,
                                    return_data=return_field)
    result = response.return_data[0]
    return result