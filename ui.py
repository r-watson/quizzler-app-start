from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # set QuizBrain as required datatype for quiz_brain argument
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="test", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_method)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_method)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_method(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # pass

    def false_method(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # pass

    def give_feedback(self, is_right):
        # if is_right == "true":
        self.canvas.config(self.canvas, bg="green")
        self.window.after(1000, self.canvas.config(self.canvas, bg="white"))


