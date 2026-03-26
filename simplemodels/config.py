from typing import Any, Dict

# Конфигурация по умолчанию
"""Словарь с параметрами конфигурации по умолчанию для пайплайна генерации конформеров."""
DEFAULT_CONFIG = {
    "input_format": "smiles",  # 'smiles' или 'xyz'
    "generator_type": "ase",  # 'ase' или 'openbabel'
    "analyzer_type": "dscribe",  # 'dscribe'
    "optimizer_type": "dft",  # 'dft'
    "enable_optimization": False,  # Включить дооптимизацию
    "num_conformers": 100,  # Число конформеров
    "output_dir": "output",  # Папка для выходных файлов
    "report_path": "report.html",  # Путь к HTML-отчету
}


def load_config(config_path: str = None) -> Dict[str, Any]:
    """Загружает конфигурацию из файла или возвращает по умолчанию.

    :param config_path: Путь к YAML/JSON файлу конфигурации
    :return: Словарь конфигурации
    """
    if config_path:
        # Заглушка: Реализовать загрузку из YAML/JSON
        raise NotImplementedError("Реализовать загрузку конфигурации из файла")
    return DEFAULT_CONFIG.copy()
