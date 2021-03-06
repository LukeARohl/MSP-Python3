from struct import unpack

from msp.data_structures.data_structure import DataStructure
from msp.message_ids import MessageIDs


class PIDCoefficients(DataStructure):
    def __init__(self):
        super().__init__(MessageIDs.PID)
        self.rp = 0
        self.ri = 0
        self.rd = 0

        self.pp = 0
        self.pi = 0
        self.pd = 0

        self.yp = 0
        self.yi = 0
        self.yd = 0

    @staticmethod
    def parse(data):
        pid_coefficients = PIDCoefficients()

        raise NotImplemented("Look at data and create it.")

        pid_coefficients.rp = data[0]
        pid_coefficients.ri = data[1]
        pid_coefficients.rd = data[2]

        pid_coefficients.pp = data[3]
        pid_coefficients.pi = data[4]
        pid_coefficients.pd = data[5]

        pid_coefficients.yp = data[6]
        pid_coefficients.yi = data[7]
        pid_coefficients.yd = data[8]

        return pid_coefficients

    def serialize(self, data=None) -> bytes:
        # Check if Setting or Getting
        if not data:
            # If getting use super's serialize
            return super().serialize()

        raise NotImplemented

        # Serialize Data
        result = int().to_bytes(1, 'little')
        result += int(MessageIDs.SET_PID).to_bytes(1, 'little')

        # Serialize Checksum
        result = DataStructure.get_header() + result + DataStructure.perform_checksum(result)

        # Return result
        return result

