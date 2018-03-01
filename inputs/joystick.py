
import pygame

class Joysticks():
    def __init__(self):
        self.stick = None
        if pygame.joystick.get_count() == 1:
            print "db 1 joystick found... proceeding..."
            self.stick = pygame.joystick.Joystick(0)
            self.stick.init()
            print self.stick.get_name()

            print self.stick.get_numbuttons()



    def listenJoystick(self,guy,event):

            if event.type == pygame.JOYBUTTONDOWN:
                # button down
                if self.stick.get_button(2):
                    #jump left
                    # print "db 2"
                    guy.jump(guy.LEFT)
                elif self.stick.get_button(1):
                    # print "db 1"
                    guy.jump(guy.RIGHT)
                elif self.stick.get_button(0):


                    guy.jump(guy.CENTER)

                    ##jump right
                # for i in range(self.stick.get_numbuttons()):
                #     # print "button" + self.stick.get_button(i)
                #     guy.jump()

