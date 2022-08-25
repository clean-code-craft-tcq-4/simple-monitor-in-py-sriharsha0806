from BMS.Base import BMS 

class Charge_rate(BMS):
  indicators = {
    (0, 0.75) : ("NORMAL_CHARGE_RATE", True),
    (0.76, 0.8) : ("CHARGE_RATE_WARNING", True),
    (0.81, 1) : ("CHARGE_RATE_ERROR", False)
  }
  
  @classmethod
  def health(cls, val):
    for indicator in Charge_rate.indicators.keys():
      if indicator[0] <= val <= indicator[1]:
        return Charge_rate.indicators[indicator]
  

