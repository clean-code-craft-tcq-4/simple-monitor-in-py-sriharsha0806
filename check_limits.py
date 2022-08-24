# OCP
from BMS import Temperature, Soc, Charge_rate
from translate_lan import translate_language
class main:
  @staticmethod
  def formatter(string, lan="en"):
    if lan == "de":
      print(translate_language.translation(string, destination=lan))
    else:
      print(string)
 
  @staticmethod
  def battery_is_ok(temperature, soc, charge_rate, lan="en"):
    temp_formatter, temp_bool = Temperature.health(temperature)
    soc_formatter, soc_bool = Soc.health(soc)
    charge_rate_formatter, charge_rate_bool = Charge_rate.health(charge_rate)
    features = [temp_bool, soc_bool, charge_rate_bool]
    main.formatter(temp_formatter)
    main.formatter(soc_formatter)
    main.formatter(charge_rate_formatter)
    
    if all(features):
      return True
    return False
