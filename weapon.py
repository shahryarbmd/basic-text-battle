class Weapon:
   def __init__(self, name:str, damage:int, type:str, material:str, quality:str, damage_type:str, value:int):
      self.name = name
      self.damage = damage
      self.damage_type = damage_type
      self.type = type
      self.material = material
      self.quality = quality
      self.value = value
      
fists = Weapon(name = "Fists",
              damage = 5,
              type = "unarmed",
              material= "flesh",
              quality = "common",
              damage_type= "blunt",
              value = 0)
                             
 