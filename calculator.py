from tkinter import *

window = Tk()
window.title("Calculator")

out = Entry(window, width=25, borderwidth=5)
out.grid(row=0,column=0, columnspan=2, padx=10, pady=10)

ansLabel = Entry(window, width=5)
ansLabel.grid(row=0,column=2)

calc = ""

def idk(num):
	global calc
	calc += str(num)
	out.delete(0, END)
	out.insert(0, calc)

def equate():
	global calc
	calc = calc.replace("-","+-")
	addnums = calc.split("+")
	ans = 0
	for num in addnums:
		if num[0] == "-1":
			num = num[1:-1]
			num *= -1
		try:
			num = int(num)
		except ValueError:
			pass
		else:
			try:
				ans + num
			except TypeError:
				ans = "Syntax error"
			else:
				ans += num

	ansLabel.delete(0, END)
	ansLabel.insert(0, ans)
	calc = ""

Button1 = Button(window, text="1", padx=40, pady=20, command=lambda: idk(1))
Button2 = Button(window, text="2", padx=40, pady=20, command=lambda: idk(2))
Button3 = Button(window, text="3", padx=40, pady=20, command=lambda: idk(3))
Button4 = Button(window, text="4", padx=40, pady=20, command=lambda: idk(4))
Button5 = Button(window, text="5", padx=40, pady=20, command=lambda: idk(5))
Button6 = Button(window, text="6", padx=40, pady=20, command=lambda: idk(6))
Button7 = Button(window, text="7", padx=40, pady=20, command=lambda: idk(7))
Button8 = Button(window, text="8", padx=40, pady=20, command=lambda: idk(8))
Button9 = Button(window, text="9", padx=40, pady=20, command=lambda: idk(9))
Button0 = Button(window, text="0", padx=40, pady=20, command=lambda: idk(0))
ButtonAdd = Button(window, text="+", padx=40, pady=20, command=lambda: idk("+"))
ButtonSub = Button(window, text="-", padx=40, pady=20, command=lambda: idk("-"))
ButtonEqual = Button(window, text="=", padx=40, pady=20, command=equate)


Button1.grid(row=1,column=0)
Button2.grid(row=1,column=1)
Button3.grid(row=1,column=2)
Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)
Button7.grid(row=3,column=0)
Button8.grid(row=3,column=1)
Button9.grid(row=3,column=2)
Button0.grid(row=4,column=0)
ButtonAdd.grid(row=4,column=1)
ButtonSub.grid(row=5,column=0)
ButtonEqual.grid(row=4,column=2)

window.mainloop()

funcList = ["help","add","subtract","multiply","divide","ans","e","pi","phi"]

def add(num1,num2):
	ans = num1 + num2
	return ans

def subtract(num1,num2):
	ans = num1 - num2
	return ans

def multiply(num1,num2):
	ans = num1 * num2
	return ans

def divide(num1,num2):
	ans = num1 / num2
	return ans

def e():
	e = 0
	for x in range(100):
		factorial = 1
		for i in range(x):
			factorial *= i + 1
		e += 1/factorial
	return e

ans = 0
num1 = 0
num2 = 0

while True:
	function = input(">")
	if function == "help":
		for func in funcList:
			print(func)
	if function == "add":
		num1 = float(input())
		num2 = float(input())
		ans = add(num1,num2)
		print(ans)
	if function == "subtract":
		num1 = float(input())
		num2 = float(input())
		ans = subtract(num1,num2)
		print(ans)
	if function == "multiply":
		num1 = float(input())
		num2 = float(input())
		ans = multiply(num1,num2)
		print(ans)
	if function == "divide":
		num1 = float(input())
		num2 = float(input())
		ans = divide(num1,num2)
		print(ans)
	if function == "ans":
		print(ans)
	if function == "e":
		ans = e()
		print(ans)
	if function == "pi":
		ans = pi()
		print(ans)