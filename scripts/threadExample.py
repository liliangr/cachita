import sys, time
from PyQt4 import QtCore, QtGui

class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)
  self.i = 0
  
 def load(self, value):
  self.i = value
  self.start()

 def __del__(self):
  self.wait()
 
 def run(self):
  #for i in range(6):
  self.emit( QtCore.SIGNAL('update(QString)'), "from work thread " + str(self.i) )
  #return
  
  
class MyApp(QtGui.QWidget):
 def __init__(self, parent=None):
  QtGui.QWidget.__init__(self, parent)
 
  self.setGeometry(300, 300, 280, 600)
  self.setWindowTitle('threads')
 
  self.layout = QtGui.QVBoxLayout(self)
 
  self.testButton = QtGui.QPushButton("test")
  self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)
  self.listwidget = QtGui.QListWidget(self)
 
  self.layout.addWidget(self.testButton)
  self.layout.addWidget(self.listwidget)
  
  self.threadPool = []
 
 def add(self, text):
  """ Add item to list widget """
  print "Add: " + text
  self.listwidget.addItem(text)
  self.listwidget.sortItems()
 

 def test(self):
  self.listwidget.clear()

  
  # replace in test()
  for i in range(10):
      self.threadPool.append(WorkThread())
      self.connect( self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.add )
      self.threadPool[len(self.threadPool)-1].load(i)
#      self.threadPool[len(self.threadPool)-1].start()
  return
  
# run
app = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()

