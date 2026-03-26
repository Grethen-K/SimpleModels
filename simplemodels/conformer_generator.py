from typing import Any, Dict, List

from ase import Atoms
from utils import BaseConformerGenerator


class ASEConformerGenerator(BaseConformerGenerator):
    """Генератор конформеров на основе ASE.

    Использует ASE для генерации и оптимизации конформеров.
    """

    def generate_and_save(self, atoms: Atoms, config: Dict[str, Any]) -> List[str]:
        """Генерация конформеров с ASE."""
        # Заглушка: Реализовать генерацию с ASE и сохранение в XYZ
        raise NotImplementedError("Реализовать генерацию с ASE")


class OpenBabelConformerGenerator(BaseConformerGenerator):
    """Генератор конформеров на основе OpenBabel.

    Использует OpenBabel для генерации конформеров.
    """

    def generate_and_save(self, atoms: Atoms, config: Dict[str, Any]) -> List[str]:
        """Генерация конформеров с OpenBabel."""
        # Заглушка: Реализовать генерацию с OpenBabel и сохранение в XYZ
        raise NotImplementedError("Реализовать генерацию с OpenBabel")
