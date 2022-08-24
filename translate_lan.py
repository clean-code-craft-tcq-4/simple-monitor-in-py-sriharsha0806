class translate_language:
  @staticmethod
  def translation(string, target_lang="de"):
    translate = {
      'LOW_TEMPERATURE_BREACH' : 'NIEDRIGE_TEMPERATURVERLETZUNG',
      'LOW_TEMPERATURE_WARNING' : 'WARNUNG_NIEDRIGE_TEMPERATUR',
      'NORMAL_TEMPERATURE' 'NORMALE_TEMPERATUR':,
      'HIGH_TEMPERATURE_WARNING' : 'WARNUNG_ZU_HOHER_TEMPERATUR',
      'HIGH_TEMPERATURE_BREACH' : 'HOHE_TEMPERATURVERLETZUNG',
      'LOW_SOC_BREACH' : 'NIEDRIGE_SOC_VERLETZUNG',
      'LOW_SOC_WARNING' : 'WARNUNG_NIEDRIGE_SOC',
      'NORMAL_SOC' : 'NORMALE_SOC',
      'HIGH_SOC_WARNING' : 'WARNUNG_ZU_HOHER_SOC',
      'HIGH_SOC_BREACH' : 'HOCH_SOC_WARNING',
      'NORMAL_CHARGE_RATE' : 'NORMALE_LADERATE',
      'CHARGE_RATE_WARNING' : 'LADESTROM_WARNUNG',
      'CHARGE_RATE_ERROR' : 'LADESTROM_ERROR',
    }
    return translate.get(string)

