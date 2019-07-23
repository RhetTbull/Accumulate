import ui
from datetime import datetime, time
import time

#TODO: Add logging
#TODO: Add finished when stopped or reach timer
#TODO: Add adjustment of goal time

class CustomUIView(ui.View):
	def __init__(self):
		#self.color = 'red'
		#touch event are limited to this area (left=100,top=100,right=200,bottom=200)
		self.color_rest = '#ff7272'
		self.color_work = '#46d176'
		self.color_default = 'white'
		#self.x = 0
		#self.y = 0
		#self.height = 480
		#self.width = 320
		self.timeSet = 300 # seconds
		self.timeCounter = 0
		self.timePaused = 0
		self.view = ui.load_view('Accum.pyui')
		self.view.present('sheet')
		self.view.name = 'AwesomeTimer'
		self.started = False
		self.paused = False
		self.view['btnStop'].enabled = False
		self.view['btnPause'].enabled = False
		
#	def draw(self):
#		#if the path is larger then 100x100 it will be clipped
#		#path = ui.Path.rect(0, 0, 100, 100)
#		#ui.set_color(self.color)
#		#path.fill()
#		#__super__.draw(self)
#		pass


#	def touch_ended(self, touch):
##		if self.color == 'green':
##			self.color = 'blue'
##		else:
##			self.color = 'red'
#		self.set_needs_display()
#		
#	def touch_began(self, touch):
##		self.color = 'green'
#		self.color = 'blue'
#		self.set_needs_display()


#class SpecialButton(object):
#	def __init__(self):
#		self.view = ui.load_view('SpecialButton')
#		self.view.present('fullscreen')
#		self.btn = MyButtonClass()
#		self.view.add_subview(self.btn)

	def btnStart(self, sender):
		self.started = True
		#self.paused = False
		#self.timeStart = datetime.now()
		#self.timeStart = time.time()
		#self.set_needs_display()
#		timeCounter = self.view['timeCounter']
#		timeCounter.text = 'foo'
		self.view['btnStart'].enabled = False
		self.view['btnStop'].enabled = True
		self.view['btnPause'].enabled = True
		if self.paused:
			self.view.background_color = self.color_rest
			self.updatePaused()
		else:
			self.view.background_color = self.color_work
			self.updateTimer()
		
	def btnStop(self, sender):
		self.started = False
		#self.paused = False
		self.view['btnStop'].enabled = False
		self.view['btnStart'].enabled = True
		self.view['btnPause'].enabled = False
		#self.view['timeCounter'].background_color='white'
		self.view.background_color = self.color_default
		pass
	
	def btnPause(self, sender):
		#todo: how to to a pythonic flip-flop?
		if self.paused:
			self.paused = False
			self.timePausedBegan = None
			self.updateTimer()
			sender.title="Rest"
			#sender.image=ui.Image.named("ios7_pause_24")
			#img = ui.Image.named("ios7_pause_24")
			#img.show()
			self.view.background_color=self.color_work
		else:
			self.paused = True
			sender.title="Work"
			#sender.image=ui.Image.named("play_24")
#			self.timePausedBegan = time.time()
			self.view.background_color = self.color_rest
			self.updatePaused()
			
		
	@ui.in_background
	def updateTimer(self):
		timeStart = time.perf_counter()
		#self.view['timeCounter'].background_color='green'
		while(self.started and not self.paused and self.timeCounter <= self.timeSet):
			#self.timeCounter = datetime.now() - self.timeStart
			now = time.perf_counter()
			delta = now - timeStart
			self.timeCounter += delta
			minutes = int(self.timeCounter / 60)
			seconds = int(self.timeCounter - minutes * 60)
			#print(f"{self.timeCounter},{minutes},{seconds}")
			strtime = "{0:01d}:{1:02d}".format(int(minutes),int(seconds))
			#print(strtime)
			self.view['timeCounter'].text = strtime
			timeStart = time.perf_counter()
			time.sleep(0.10)
			
			
	@ui.in_background
	def updatePaused(self):
		timePausedBegan = time.perf_counter()
		#self.view['timePaused'].tint_color = 'red'
		while(self.paused and self.started):
			now = time.perf_counter()
			delta = now - timePausedBegan
			#print(f"timePaused = {self.timePaused}, began = {timePausedBegan}, now = {now}, delta={delta}")
			self.timePaused += delta
			#print(f"timePaused = {self.timePaused}, delta={delta}")
			minutes = int(self.timePaused / 60)
			seconds = int(self.timePaused - minutes * 60)
			#print(f"timePaused = {self.timePaused}, delta={delta}, began={timePausedBegan} {minutes}, {seconds}")
			strtime = "{0:01d}:{1:02d}".format(int(minutes),int(seconds))
			#print(strtime)
			self.view['timePaused'].text = strtime
			timePausedBegan = time.perf_counter()
			time.sleep(0.10)
				
CustomUIView()
#me_counter = v['timeCounter']

