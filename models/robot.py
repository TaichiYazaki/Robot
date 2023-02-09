DEFAULT_ROBOT_NAME = 'roboko'

        
class Robot(object):

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name
        
    def hello(self):
        with open('templates/hello.txt') as template_file:
            file = template_file.read()
            insert_robot_name =file.replace('$robot_name',self.name)
            user_name = input(insert_robot_name)
            self.user_name = user_name.title()
            

class RestaurantRobot(Robot):

    def __init__(self, name=DEFAULT_ROBOT_NAME,):
        super().__init__(name)

    def decorator(func):
        def wrapper(*args, **kw):
            print('デコレーター開始')
            func(*args, **kw)
        return wrapper

    @decorator
    def ask_user_favorite(self):
        with open('templates/whitch_restaurant.txt') as template_file:
            file = template_file.read()
            insert_user_name = file.replace('$user_name', self.user_name)
            recommend_restaurant = input(insert_user_name)
