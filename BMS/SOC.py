from BMS.Base import BMS

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