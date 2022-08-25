from BMS.Base import BMS

class Temperature(BMS):
  indicators = {
    (-273, 0) : ("LOW_TEMPERATURE_BREACH", False),
    (0, 3) : ("LOW_TEMPERATURE_WARNING", True),
    (3, 42) : ("NORMAL_TEMPERATURE", True),
    (42, 45) : ("HIGH_TEMPERATURE_WARNING", True),
    (45, 100) : ("HIGH_TEMPERATURE_BREACH", False)
  }
  
  @classmethod
  def health(cls, val):
    for indicator in Temperature.indicators.keys():
      if val in range(*indicator):
        return Temperature.indicators[indicator]