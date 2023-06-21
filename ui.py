from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizlerr")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 15, "normal")
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question text here.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_Img = PhotoImage(file="images/true.png")
        self.true_Btn = Button(image=true_Img, highlightthickness=0)
        self.true_Btn.grid(row=2, column=0)

        wrong_Img = PhotoImage(file="images/false.png")
        self.wrong_Btn = Button(image=wrong_Img, highlightthickness=0)
        self.wrong_Btn.grid(row=2, column=1)

        self.window.mainloop()

