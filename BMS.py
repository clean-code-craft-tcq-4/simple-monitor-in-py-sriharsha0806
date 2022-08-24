class BMS:
  def __init__(self, feature):
    self._feature = feature
    
  @staticmethod
  def health(val):
    pass
  
class temperature(BMS):
  @staticmethod
  def health(val):
    if val not in range(46):
      print("Temperature is out of range")
      return False
    return True
  
class soc(BMS):
  @staticmethod
  def health(val):
    if val not in range(20, 81):
      print("State of Charge is out of range")
      return False
    return True
  
class charge_rate(BMS):
  @staticmethod
  def health(val):
    if val not in range(0.8):
       print("Charge is out of range")
      return False
    return True
