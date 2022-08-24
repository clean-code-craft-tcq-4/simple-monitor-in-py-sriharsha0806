class BMS:    
  @classmethod
  def health(cls):
    pass
  
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
         
class Soc(BMS):
  indicators = {
    (0, 20) : ("LOW_SOC_BREACH", False),
    (21, 24) : ("LOW_SOC_WARNING", True),
    (24, 75) : ("NORMAL_SOC", True),
    (76, 80) : ("HIGH_SOC_WARNING", True),
    (81, 100) : ("HIGH_SOC_BREACH", False)
  }

  @classmethod
  def health(cls, val):
    for indicator in Soc.indicators.keys():
      if val in range(*indicator):
        return Soc.indicators[indicator]
  
class Charge_rate(BMS):
  indicators = {
    (0, 0.75) : ("NORMAL_CHARGE_RATE", True),
    (0.76, 0.8) : ("CHARGE_RATE_WARNING", True),
    (0.81, 1) : ("CHARGE_RATE_ERROR", False)
  }
  
  @classmethod
  def health(cls, val):
    for indicator in Charge_rate.indicators.keys():
      if indicator[0] <= val and val <= indicator[1]:
        return Charge_rate.indicators[indicator]
  
