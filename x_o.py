import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
import random


# Globals
xod = 1
x_list = []
o_list = []
check_list = [
    ['b1', 'b2', 'b3'], ['b4', 'b5', 'b6'], ['b7', 'b8', 'b9'],
    ['b1', 'b5', 'b9'], ['b3', 'b5', 'b7'], ['b1', 'b4', 'b7'],
    ['b2', 'b5', 'b8'], ['b3', 'b6', 'b9'],
]



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui.ui', self)
        for n in range(1, 10):
            getattr(self, 'b%s' % n).pressed.connect(self.press_button)

    # Set value on the field
    def press_button(self):
        global xod, x_list, o_list
        print(xod)
        if xod % 2 == 0:
            
            # If field is empty you can setup value
            # Sender() used to determine the currently pressed button
            if self.sender().text() == '':
                # Setup value 'X' in the button
                self.sender().setText('x')
                # Pass the move
                xod += 1
                # Add the name of the button to the list
                # to find out the winner in the future
                x_list.append(self.sender().objectName())
                self.result()

                print(self.sender())
                
            else:

                print('err')
        else:

            # The same actions for the next turn
            if self.sender().text() == '':
                self.sender().setText('o')
                xod += 1
                o_list.append(self.sender().objectName())
                self.result()

                # comment out the 2 following lines to disable ai
                # self.ai_move()
                # xod += 1
                
            else:
                print('err')
                
              

    # Calculating the results.
    # Check if there are matches
    # from both lists of moves with
    # the list of possible options for winning
    def result(self):
        global x_list, o_list, check_list
        x = 0
        o = 0
        for i in range(8):
            for j in range(3):
                if check_list[i][j] in x_list:
                    x += 1
                else:
                    x = 0
            if x >= 3:
                print('WIN')
                self.end_game()



        for i in range(8):
            for j in range(3):
                if check_list[i][j] in o_list:
                    o += 1
                else:
                    o = 0
            if o >= 3:
                print('WIN')
                self.end_game()

        text_list = []
        for n in range(1, 10):
        	text = getattr(self, 'b%s' % n).text() == ''
        	text_list.append(text)
        if not True in text_list:

        	self.end_game()

    def ai_move(self):
        global xod, check_list
        field_list = []
        for n in range(1, 10):
            field_list.append(getattr(self, 'b%s' % n))
        if xod == 2:
            if field_list[4].text() == '':
                btn = field_list[4]
                btn.setText('x')
                self.result()
            else:
                del field_list[4]
                btn = random.choice(field_list)
                btn.setText('x')
                self.result()
        elif xod >= 4:
            empty_fields = []
            for field1 in field_list:
                if field1.text() == '':
                    empty_fields.append(field1)
                    print(empty_fields)
            btn = random.choice(empty_fields)
            btn.setText('x')
            self.result()
            # p = getattr(self, empty_fields[0])
            # p.setText('x')

            

  	# End game function show the window that asks if i want to play again 
    def end_game(self):
    	global xod, x_list, o_list
  		# Message window call
    	question = QtWidgets.QMessageBox.question(self, 'Игра окончена!', 
    		'Еще раз?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    	# If Yes pressed 
    	if question == QtWidgets.QMessageBox.Yes:
            xod = 0
            x_list = []
            o_list = []
            for n in range(1, 10):
            	getattr(self, 'b%s' % n).setText('')
    	else:
		    sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
