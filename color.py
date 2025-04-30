
from typing import Dict

class ColorCoefficient:
   
    _COEFFICIENTS: Dict[str, float] = {
        "белый": 1.0,
        "синий": 1.0,
        "желтый": 1.1,
        "красный": 1.0,
        "перламутровый": 1.2,
        "серый металлик": 1.3,
    }

    @classmethod
    def get(cls, color: str) -> float:
        return cls._COEFFICIENTS.get(color.lower().strip(), 1.0)
