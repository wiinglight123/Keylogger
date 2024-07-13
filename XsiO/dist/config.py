import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.image = Image.open("image.jpeg")
        self.image = self.image.resize((500, 150))
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.grid(row=4, column=0, columnspan=3)


    def click(self, i, j):
        if self.buttons[i][j]['text'] == '':
            self.buttons[i][j]['text'] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != '':
                return True
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != '':
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
                return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == '':
                    return False
        return True

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button['text'] = ''
        self.player = 'X'

    def run(self):
        self.root.mainloop()

root = tk.Tk()
game = TicTacToe(root)
game.run()