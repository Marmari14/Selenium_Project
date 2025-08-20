import logging
from datetime import datetime
import os


def setup_logger(name, log_level=logging.INFO):
	"""Настройка логгера для Selenium тестов"""

	# Создаем папку для логов если ее нет
	log_dir = "logs"
	os.makedirs(log_dir, exist_ok=True)

	# Формат логов
	formatter = logging.Formatter(
		'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		datefmt='%d-%m-%Y %H:%M:%S'
	)

	# Имя файла с текущей датой
	log_file = os.path.join(log_dir, f'log_{datetime.now().strftime("%d%m%Y")}.log')

	# Создаем логгер
	logger = logging.getLogger(name)
	logger.setLevel(log_level)

	# Обработчик для записи в файл
	file_handler = logging.FileHandler(log_file, encoding='utf-8')
	file_handler.setFormatter(formatter)

	# Обработчик для вывода в консоль
	console_handler = logging.StreamHandler()
	console_handler.setFormatter(formatter)

	# Добавляем обработчики
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)

	return logger