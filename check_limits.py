from BMS import Temperature, Soc, Charge

class main:
  @staticmethod
  def battery_is_ok(temperature, soc, charge_rate):
    temp_res = Temperature.health(temperature)
    soc_res = Soc.health(soc)
    charge_res = Charge.health(charge_rate)
    if temp_res and soc_res and charge_res:
      return True
    return False

  
  



