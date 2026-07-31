"""
Klient Modbus TCP - odczytuje dane z symulatora i wyświetla je w konsoli.
"""

from pyModbusTCP.client import ModbusClient
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Połączenie z symulatorem
client = ModbusClient(host="127.0.0.1", port=5020, auto_open=True)

if not client.is_open:
    logger.error("Nie można połączyć się z symulatorem. Uruchom simulator.py najpierw.")
    exit(1)

logger.info("Połączono z symulatorem Modbus TCP.")

try:
    while True:
        # Odczytaj 4 rejestry holding (adres 0, liczba 4)
        registers = client.read_holding_registers(0, 4)
        
        if registers:
            temp = registers[0] / 10.0
            hum = registers[1] / 10.0
            voltage = registers[2] / 10.0
            mode = registers[3]
            
            modes = {0: "Wyłączony", 1: "Grzanie", 2: "Chłodzenie"}
            mode_str = modes.get(mode, "Nieznany")
            
            print(f"Temperatura: {temp:.1f}°C | Wilgotność: {hum:.1f}% | Napięcie: {voltage:.1f}V | Tryb: {mode_str}")
        else:
            logger.warning("Błąd odczytu rejestrów.")
        
        time.sleep(2)  # Odczyt co 2 sekundy

except KeyboardInterrupt:
    logger.info("Zatrzymano odczyt.")