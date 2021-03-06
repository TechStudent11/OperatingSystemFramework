from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Widget:
	def __init__(self, surface=None, **kwargs):
		self.master = surface
		self.options = kwargs

	def _create(self, widget, x=0, y=0, **kwargs):
		self.x = x
		self.y = y

		self.surface = Frame(self.master)

		self.widget = widget(self.surface, **kwargs)
		self.widget.pack()

		self.surface.place(x=self.x, y=self.y)

	def center(self):
		self.surface.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")

class InheirtWidget(Widget):
	def __init__(self, surface=None, x=0, y=0, **kwargs):
		super().__init__(surface)

		self.master = surface

		self.x = x
		self.y = y

		self.options = kwargs


class Textbox(InheirtWidget):
	def __init__(self, surface=None, text=None, x=0, y=0, **kwargs):
		super().__init__(surface, x, y, **kwargs)

		self.text = text

		self._create(Label, self.x, self.y, text=self.text, **self.options)

class TextInputBox(InheirtWidget):
	def __init__(self, surface=None, multiline=False, x=0, y=0, **kwargs):
		super().__init__(surface, x, y, **kwargs)

		self.multiline = multiline

		if self.multiline:
			self._create(ScrolledText, self.x, self.y, **self.options)
		else:
			self.stringVar = StringVar()
			self._create(Entry, self.x, self.y, textvariable=self.stringVar, **self.options)

	def get(self, start=1.0, end=END):
		if self.multiline:
			output = self.widget.get(start, end)
		else:
			output = self.widget.get()

		return output
	
	def insert(self, text="", index="1.0"):
		if self.multiline:
			self.widget.insert(index, text)
		else:
			self.widget.insert(0, text)

	def clear(self):
		if self.multiline:
			self.widget.delete(1.0, END)
		else:
			self.widget.delete(0, END)

class PushButton(InheirtWidget):
	def __init__(self, surface=None, text=None, command=lambda: print(""), x=0, y=0, **kwargs):
		super().__init__(surface, x, y, **kwargs)

		self.text = text
		self.command = command

		self._create(Button, self.x, self.y, text=self.text, command=self.command, **self.options)