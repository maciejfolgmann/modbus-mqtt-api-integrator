"""
Symulator urządzenia Modbus TCP.
Uruchamia serwer na localhost:5020 z 4 rejestrami holding:
- Rejestr 0: temperatura (wartość x10, np. 250 = 25.0°C)
- Rejestr 1: wilgotność (wartość x10, np. 550 = 55.0%)
- Rejestr 2: napięcie (wartość x10, np. 230 = 230V)
- Rejestr 3: tryb pracy (0 = wyłączony, 1 = grzanie, 2 = chłodzenie)
"""

from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore.context import ModbusServerContext, ModbusSlaveContext
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 10),
    co=ModbusSequentialDataBlock(0, [0] * 10),
    hr=ModbusSequentialDataBlock(0, [250, 550, 230, 0]),
    ir=ModbusSequentialDataBlock(0, [0] * 10)
)

context = ModbusServerContext(slaves=store, single=True)

if __name__ == "__main__":
    logger.info("Uruchamiam symulator Modbus TCP na 127.0.0.1:5020...")
    StartTcpServer(context, address=("127.0.0.1", 5020))