import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Función para configurar el logger."""
    logger = logging.getLogger(name)
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(level)

    return logger

# Ejemplo de uso
if __name__ == "__main__":
    logger = setup_logger('example_logger', 'example.log')
    logger.info('Logger is set up and ready to go!')
