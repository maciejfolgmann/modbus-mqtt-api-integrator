"""
Symulator urządzenia Modbus TCP.
Uruchamia serwer na localhost:5020 z 4 rejestrami holding:
- Rejestr 0: temperatura (x10, np. 250 = 25.0°C)
- Rejestr 1: wilgotność (x10, np. 550 = 55.0%)
- Rejestr 2: napięcie (x10, np. 230 = 230V)
- Rejestr 3: tryb pracy (0=off, 1=grzanie, 2=chłodzenie)
"""

from pyModbusTCP.server import ModbusServer, DataBank
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tworzymy bank danych z początkowymi wartościami
server = ModbusServer(host="127.0.0.1", port=5020, no_block=True)

# Ustawiamy wartości początkowe rejestrów holding
server.data_bank.set_holding_registers(0, [250, 550, 230, 0])

if __name__ == "__main__":
    logger.info("Uruchamiam symulator Modbus TCP na 127.0.0.1:5020...")
    server.start()
    logger.info("Symulator działa. Zatrzymaj Ctrl+C.")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop()
        logger.info("Symulator zatrzymany.")