from car1 import Car


class Battery():
        
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):#新增的办法做了一个简单的分析
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif sef.battery_size ==85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += "miles on a full range"
        print(message)
    
class ElectricCar(Car):
    
    def __init__(self, make,model,year):
        #初始化父类属性
        super().__init__(make, model, year)
        self.battery = Battery()
        