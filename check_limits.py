from BMS import Temperature, Soc, Charge_rate

class main:
  @staticmethod
  def battery_is_ok(temperature, soc, charge_rate):
    temp_bool = Temperature.health(temperature)
    soc_bool = Soc.health(soc)
    charge_bool = Charge_rate.health(charge_rate)
    if temp_bool and soc_bool and charge_rate_bool:
      return True
    return False

  
  



