from BMS import Temperature, Soc, Charge_rate

class main:
  @staticmethod
  def battery_is_ok(temperature, soc, charge_rate):
    temp_bool = Temperature.health(temperature)
    soc_bool = Soc.health(soc)
    charge_bool = Charge_rate.health(charge_rate)
    features = [temp_bool, soc_bool, charge_rate_bool]
    if not any(features):
      return True
    return False

  
  



