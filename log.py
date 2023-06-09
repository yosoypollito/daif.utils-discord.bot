from enum import Enum
class Feature(Enum):
    Command = "COMMAND"
    Service = "SERVICE"
    
class Log:
  def __init__(self, prefix: str, feature: Feature):
    self.prefix = prefix
    self.feature = feature 
  
  def info(self, *args: any):
    log_info = f"{self.prefix.capitalize()} {self.feature.value}"
    print(f"[{log_info}]\n{' '.join(map(str, args))}\n[END {log_info}]")
  
  def error(self, *args):
    # TODO handle errors logs
    self.info(args)