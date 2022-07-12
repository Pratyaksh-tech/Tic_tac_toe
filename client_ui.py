from tkinter import *
import threading

root = Tk();
root.geometry("350x450");
root.title("tac");


head = Label(root, text="Tic-Tac-Toe", font=("Arial", 25, "bold"))
head.pack();

frame_main = Frame(root, width=340, height=401, bd=4, relief=RIDGE, background="white");
frame_main.pack();

width_of_btn1 = 14;
height_of_btn1 = 6;

row_of_bt1 = 0;
column_of_btn1 = 0;

pressed = True;

def show_res(btn):
	global pressed;
	if pressed == True and btn["text"] == "":
		btn["text"] = "X";
		pressed = False;
	elif pressed == False and btn["text"] == "":
		btn["text"] = "O";
		pressed = True;

	global btn1;
	global btn2;
	global btn3;
	global btn4;
	global btn5;
	global btn6;
	global btn7;
	global btn8;
	global btn9;

btn1 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn1));
btn1.grid(row=0, column=0);

btn2 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn2));
btn2.grid(row=0, column=1);

btn3 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn3));
btn3.grid(row=0, column=2);

btn4 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn4));
btn4.grid(row=1, column=0);

btn5 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn5));
btn5.grid(row=1, column=1);

btn6 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn6));
btn6.grid(row=1, column=2);

btn7 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn7));
btn7.grid(row=2, column=0);

btn8 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn8));
btn8.grid(row=2, column=1);

btn9 = Button(frame_main, width=width_of_btn1, height=height_of_btn1, background="white", command=lambda: show_res(btn9));
btn9.grid(row=2, column=2);


winner = "";
def check_res():
	global winner;
	while True:
		if btn1["text"] != "":
			if btn1["text"] == btn2["text"] == btn3["text"]:
				btn1["background"] = "lightgreen"
				btn2["background"] = "lightgreen"
				btn3["background"] = "lightgreen"
				winner = btn1["text"];
				break;
		
		if btn4["text"] != "":	
			if btn4["text"] == btn5["text"] == btn6["text"]:
				btn4["background"] = "lightgreen"
				btn5["background"] = "lightgreen"
				btn6["background"] = "lightgreen"
				winner = btn4["text"];
				break;
		
		if btn7["text"] != "":	
			if btn7["text"] == btn8["text"] == btn9["text"]:
				btn7["background"] = "lightgreen"
				btn8["background"] = "lightgreen"
				btn9["background"] = "lightgreen"
				winner = btn7["text"];
				break;
		
		if btn1["text"] != "":
			if btn1["text"] == btn4["text"] == btn7["text"]:
				btn1["background"] = "lightgreen"
				btn4["background"] = "lightgreen"
				btn7["background"] = "lightgreen"
				winner = btn1["text"];
				break;
		
		if btn2["text"] != "":	
			if btn2["text"] == btn5["text"] == btn8["text"]:
				btn2["background"] = "lightgreen"
				btn5["background"] = "lightgreen"
				btn8["background"] = "lightgreen"
				winner = btn2["text"];
				break;
		
		if btn3["text"] != "":	
			if btn3["text"] == btn6["text"] == btn9["text"]:
				btn3["background"] = "lightgreen"
				btn6["background"] = "lightgreen"
				btn9["background"] = "lightgreen"
				winner = btn3["text"];
				break;
		
		if btn1["text"] != "":	
			if btn1["text"] == btn5["text"] == btn9["text"]:
				btn1["background"] = "lightgreen"
				btn5["background"] = "lightgreen"
				btn9["background"] = "lightgreen"
				winner = btn1["text"];
				break;
		
		if btn3["text"] != "":	
			if btn3["text"] == btn5["text"] == btn7["text"]:
				btn3["background"] = "lightgreen"
				btn5["background"] = "lightgreen"
				btn7["background"] = "lightgreen"
				winner = btn3["text"];
				break;									

def play_again_func():
	btn1["background"] = "white";
	btn2["background"] = "white";
	btn3["background"] = "white";
	btn4["background"] = "white";
	btn5["background"] = "white";
	btn6["background"] = "white";
	btn7["background"] = "white";
	btn8["background"] = "white";
	btn9["background"] = "white";

	btn1["state"] = "active";
	btn2["state"] = "active";
	btn3["state"] = "active";
	btn4["state"] = "active";
	btn5["state"] = "active";
	btn6["state"] = "active";
	btn7["state"] = "active";
	btn8["state"] = "active";
	btn9["state"] = "active";

	btn1["text"] = "";
	btn2["text"] = "";
	btn3["text"] = "";
	btn4["text"] = "";
	btn5["text"] = "";
	btn6["text"] = "";
	btn7["text"] = "";
	btn8["text"] = "";
	btn9["text"] = "";

	pressed = True;
	show_winner.destroy();
	#play_again.destroy();
	winner = "";
	print("what is " + winner)

def check_winner():			
	global show_winner;
	#global play_again;	
	print(winner + "is winner")
	while True:
		if winner != "": 
			
			show_winner = Label(root, text=winner+" is the winner", font=("Arial", 25, "bold"));
			show_winner.pack();
			
			#play_again = Button(root, text="Play Again", font=("Arial", 14), command=play_again_func);
			#play_again.pack();
			
			btn1["state"] = "disabled";
			btn2["state"] = "disabled";
			btn3["state"] = "disabled";
			btn4["state"] = "disabled";
			btn5["state"] = "disabled";
			btn6["state"] = "disabled";
			btn7["state"] = "disabled";
			btn8["state"] = "disabled";
			btn9["state"] = "disabled";
			
			break;

play_again = Button(root, text="Play Again", font=("Arial", 14), command=play_again_func);
play_again.pack();

global thread1, thread2
thread1 = threading.Thread(target=check_res);
thread1.start();

thread2 = threading.Thread(target=check_winner);
thread2.start();

root.mainloop();