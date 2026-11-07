class LaserClass: 
    
    def __init__(self, initial_power=100): 
        self.remaining_power = initial_power
        self.direction = 0 
        pass
    def turn_right(self): 
        self.direction += 15 
        pass 
    def turn_left(self): 
        self.direction -= 15
        pass 
    def fire(self): 
        if self.remaining_power >= 10: 
            self.remaining_power = self.remaining_power - 10 
            return True 
        else:
            return False 
    pass 
class RechargeableLaser(LaserClass): 
    def __init__(self, initial_power = 100): 
        self.remaining_power = initial_power  
        self.direction = 0 
        self.max_power = initial_power  
        pass
    def recharge(self):  
         self.remaining_power =  self.max_power   


# myLaser1 = LaserClass()
# myLaser1.turn_right() 
# returned_value = myLaser1.fire() 
# myLaser1.fire
pass 

