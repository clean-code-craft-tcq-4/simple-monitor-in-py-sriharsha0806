class BMS:
  def __init__(self, feature):
    self._feature = feature
    
  @staticmethod
  def health(val):
    pass
  
class Temperature(BMS):
  @staticmethod
  def health(val):
    if val not in range(46):
      print("Temperature is out of range")
      return False
    return True
  
class Soc(BMS):
  @staticmethod
  def health(val):
    if val not in range(20, 81):
      print("State of Charge is out of range")
      return False
    return True
  
class Charge_rate(BMS):
  @staticmethod
  def health(val):
    if val not in range(0.8):
       print("Charge is out of range")
       return False
    return True
