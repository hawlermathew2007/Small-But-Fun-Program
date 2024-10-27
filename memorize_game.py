from tkinter import *
import random

def button_press(num):
	
	global text

	text += str(num)

	txt.set(text)

def activate():
	global count

	def temp():
		label.config(text= " ")

	def enter_result():
		label.config(text= "ENTER YOUR ANSWER")
		start.config(state= DISABLED)
		submit.config(state= ACTIVE)

	def randsnl():
		global count
		global answer

		if count < _max:
			window.after(200,temp)
			rand = random.choice(nums)
			label.config(text= rand)
			answer += str(rand)
			count += 1
			window.after(time,randsnl)
		else:
			window.after(200, enter_result)
			print("yea")
		print(answer, count, time, _max)

	text = ""
	txt.set(text)

	start.config(text="START")
	start.config(state=DISABLED)
	submit.config(state= DISABLED)

	if count == _max or count == _max - 1:
		count = 0
		print("yeah")
	randsnl()

def submit():
	global text 
	global answer

	if text == answer and text != "" and answer != "":
		label.config(text= "CORRECT")
		if time < 400 and _max > 10:
			txt.set("NICE! IT WILL GET HARDER IN NO TIME!")
		else:
			txt.set("WELL DONE YOU REACH THE MAX LEVEL")
		start.config(state= ACTIVE)
		count = 0
		harder()
	elif answer == "":
		text = ""
		txt.set("PLEASE PRESS START")
	else:
		start.config(text="RESTART")
		start.config(state= ACTIVE)
		label.config(text= "INCORRECT")
		txt.set("PRESS RESTART")
	text = ""
	answer = ""

def delete():
	global text
	text = ""
	txt.set(text)

def harder():		#nums and time
	global time
	global _max

	if time > 400:
		time -= 100

	if _max < 10:
		_max += 1

window = Tk()
window.title("Memorizing Game")
window.config(bg="#ffffff")
buttons = [[0,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,0,0,0,0,0]]
list_but = []
final_but = []
nums = [1,2,3,4,5,6,7,8,9,"A","B","C","D","E","@","&","#","$"]
time = 1000
_max = 5
count = 0

txt = StringVar()
text = ""
answer = ""

m_g = Label(window, text="MEMORIZING GAME", font= ("Impact", 60), padx=300, pady= 10, bg="#ededed")
m_g.pack()

line = Label(window, text= "______________________________________________________________________________________________________________________________________________________",bg="#ffffff")
line.pack()

label = Label(window, text="PRESS START", font= ("Impact",40), padx=20, pady= 10, bg="#ffffff")
label.pack()

button_frame = Frame(window, bg="#ffffff")
button_frame.pack()

start = Button(button_frame, text="START", font= ("Impact",20), state= ACTIVE,command=activate)
start.pack(side=LEFT)

block_b = Label(button_frame, text= "   ",bg="#ffffff")
block_b.pack(side=LEFT)

submit = Button(button_frame, text="SUBMIT", font= ("Impact",20), command= submit)
submit.pack(side=LEFT)

block_but = Label(button_frame, text= "   ",bg="#ffffff")
block_but.pack(side=LEFT)

delete = Button(button_frame, text="DELETE",font= ("Impact",20), command= delete)
delete.pack(side=LEFT)

block = Label(window,bg="#ffffff")
block.pack()

display = Label(window,textvariable=txt, font=("Consolas",20),bg='white',width=52,height=2,padx=2,justify=LEFT, relief=GROOVE, bd= 5)
display.pack()

frame = Frame(window, pady=20, bg= "#d0d0d0")
frame.pack()

# maybe can use for loop here

i = 0
for row in range(len(buttons)):
	for column in range(len(buttons[row])):
		buttons[row][column] = Button(frame, text=nums[i], font= ("Consolas",40), width= 4, height=1)
		buttons[row][column].grid(row= row, column= column)
		list_but.append(buttons[row][column])
		i += 1

list_but[0].config(command= lambda: button_press(nums[0]))
list_but[1].config(command= lambda: button_press(nums[1]))
list_but[2].config(command= lambda: button_press(nums[2]))
list_but[3].config(command= lambda: button_press(nums[3]))
list_but[4].config(command= lambda: button_press(nums[4]))
list_but[5].config(command= lambda: button_press(nums[5]))
list_but[6].config(command= lambda: button_press(nums[6]))
list_but[7].config(command= lambda: button_press(nums[7]))
list_but[8].config(command= lambda: button_press(nums[8]))
list_but[9].config(command= lambda: button_press(nums[9]))
list_but[10].config(command= lambda: button_press(nums[10]))
list_but[11].config(command= lambda: button_press(nums[11]))
list_but[12].config(command= lambda: button_press(nums[12]))
list_but[13].config(command= lambda: button_press(nums[13]))
list_but[14].config(command= lambda: button_press(nums[14]))
list_but[15].config(command= lambda: button_press(nums[15]))
list_but[16].config(command= lambda: button_press(nums[16]))
list_but[17].config(command= lambda: button_press(nums[17]))

for i in range(len(list_but)):
	list_but[i].config(command= lambda: button_press(nums[i]))

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (750 / 2))
y = int((screen_height / 2) - (750 / 1.75))

window.geometry(f'{750}x{750}+{x}+{y}')

window.mainloop()