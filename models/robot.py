DEFAULT_ROBOT_NAME = 'roboko'

        
class Robot(object):

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name
        
    def hello(self):
        with open('templates/hello.txt') as template_file:
            file = template_file.read()
            insert_robot_name =file.replace("$robot_name",self.name)
            user_name = input(insert_robot_name)
            self.user_name = user_name.title()
            
