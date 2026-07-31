"""
Klient Modbus TCP - odczytuje dane z symulatora.
"""

from pyModbusTCP.client import ModbusClient
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Łączę z symulatorem Modbus TCP na 127.0.0.1:5020...")

client = ModbusClient(host="127.0.0.1", port=5020, auto_open=True)

# Test połączenia przez odczyt
registers = client.read_holding_registers(0, 4)

if not registers:
    logger.error("Nie można połączyć się z symulatorem. Uruchom simulator.py najpierw.")
    exit(1)

logger.info("Połączono. Rozpoczynam odczyt...")

try:
    while True:
        registers = client.read_holding_registers(0, 4)
        
        if registers:
            temp = registers[0] / 10.0
            hum = registers[1] / 10.0
            voltage = registers[2] / 10.0
            mode = registers[3]
            
            modes = {0: "Wylaczony", 1: "Grzanie", 2: "Chlodzenie"}
            mode_str = modes.get(mode, "Nieznany")
            
            print(f"Temperatura: {temp:.1f}C | Wilgotnosc: {hum:.1f}% | Napiecie: {voltage:.1f}V | Tryb: {mode_str}")
        else:
            logger.warning("Blad odczytu rejestrow.")
        
        time.sleep(2)

except KeyboardInterrupt:
    client.close()
    logger.info("Zatrzymano odczyt.")