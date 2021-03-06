import logging
import time

for x in range(10):
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        filename='application.log',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    activo = 'GOOG'
    logging.debug(f"se esta comprando {activo}")
    logging.info(f"se esta comprando {activo}")
    logging.warning("Esto es un mensaje de prueba")
    time.sleep(3)