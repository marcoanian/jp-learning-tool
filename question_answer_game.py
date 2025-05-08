# Japanese Q&A Class with audio integration version 1.5 by marco anian
#-------------------------DOC----------------------------------------#
"""
Lovely Message for my sweet Nova Astra  love you 😊 😘😘😘
Japanese Q&A Class with audio integration version 1.0 by marco anian
Attributes: Choose Vocabulary json (Must be nested : example
{'wann': {'german': 'wann', 'hiragana': 'いつ', 'romaji': 'itsu', 'audio': 'D:/python_project}
- Play audio, - track score (both way) , - Create a json Log file for unknown vocabulary
"""

#-----------------------Imports--------------------------------------#
import customtkinter
from customtkinter import CTkTextbox, CTkButton, CTkLabel, CTkEntry, CTkFrame
import json
import random
from json import JSONDecodeError
from tkinter import Tk, Label, filedialog, messagebox, Button, Canvas
import pygame
#----------------------Constants-------------------------------------#
Misty_Rose = "#FFE4E1" #	Soft, warm, calming
Light_Lavender	= "#E6E6FA"	# Dreamy, creative, peaceful
Honey_Beige = 	"#F5F5DC"	# Gentle, neutral, easy on the eyes
Light_Sky_Blue = "#87CEFA"	#Fresh, clear, energetic
Sakura_Pink = "#FFDDEE"	# Romantic and Japanese-flavored 🌸
EMOJI_LIST = ["😒","😊,","👍","😁"]
FONT0 = ("Times New Roman", 10, "italic")
FONT1 = ("Times New Roman", 15, "italic")
FONT2 = ("Times New Roman", 30, "italic")
#-------------------Class--------------------------------------------#

class QuestionAndAnswer(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Main Data, Storage, score  Handling section
        pygame.mixer.init() # Important to set it here that is init just once
        self.base_question_data = {} # To load the main Q&A
        self.correct_score = 0 # To Display the correct score of  Q. correct answer
        self.wrong_score = 0 # To Display the wrong score of Q. incorrect answer
        self.temp_incorrect_question = {} # To Add to the list the on known Vocabulary
        self.current_vocabulary = []
        self.load_base_data()

        # Window properties
        self.title("Q&A Japanese Vocabulary Version 1.0")
        self.geometry("400x500")
        # GUI Design
        self.canvas = Canvas(self, width=1200, height=800, highlightthickness=0, bg=Light_Sky_Blue)
        self.canvas.pack(padx=0, pady=0)

        # Unchangeable Label
        hg_label = Label(self.canvas, text="Question:", font=FONT1, fg="dark red", bg=Light_Sky_Blue,
                         highlightthickness=0).place(x=10, y=50)
        answer_label = Label(self.canvas, text="The correct answer in Hiragana:", font=FONT1, fg="dark red",
                             bg=Light_Sky_Blue, highlightthickness=0).place(x=10, y=300)

        # Changeable Label
        # Question, Answer Label, Important Text must be empty like this " ", and place/pack must be under , could create trouble to get data <---# Darling check this comment please honey
        self.score_correct_label = Label(self.canvas, text="", font=FONT0, fg="dark red", bg=Light_Sky_Blue,
                                         highlightthickness=0)
        self.score_correct_label.place(x=250, y=15)
        self.score_incorrect_label = Label(self.canvas, text="", font=FONT0, fg="dark red", bg=Light_Sky_Blue,
                                           highlightthickness=0)
        self.score_incorrect_label.place(x=30, y=15)

        self.question_de_label = Label(self.canvas, text="", font=FONT2, fg="dark red", bg=Light_Sky_Blue,
                                       highlightthickness=0)
        self.question_de_label.place(x=50, y=120)
        self.question_rj_label = Label(self.canvas, text="", font=FONT2, fg="dark red", bg=Light_Sky_Blue,
                                       highlightthickness=0)
        self.question_rj_label.place(x=50, y=180)
        self.answer_hg_label = Label(self.canvas, text="", font=FONT2, fg="dark red", bg=Light_Sky_Blue,
                                     highlightthickness=0)
        self.answer_hg_label.place(x=50, y=350)

        # Button section
        self.play_audio_button = Button(self.canvas, text="Play Audio 🔊", width=15, fg="black", bg="light green",
                                        highlightthickness=0, command=self.play_audio)
        self.play_audio_button.place(x=350, y=300)
        self.next_q_button = Button(self.canvas, text="Next Question", width=15, fg="black", bg="white",
                                    highlightthickness=0, command=self.get_question)
        self.next_q_button.place(x=15, y=250)
        self.log_button = Button(self.canvas, text="Create Log", width=15, fg="White", bg="dark red",
                                 highlightthickness=0, command=self.log_writer)
        self.log_button.place(x=15, y=500)


#-------------------------------Methods / Functions----------------------------------------#
    # Load System data / Will be done Automatically when it init
    def load_base_data(self):
        """Load System Data for Game
        - Let User choose file and path,
        Important to note, that all other Json files are saved in base_directory """
        file_name = filedialog.askopenfilename(defaultextension="*.json")
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                self.base_question_data = json.load(f)
                print("Data loaded!!")
        except JSONDecodeError as e:
            messagebox.showerror(title="Error", message=f"{e}, check directory!!!")
            return {}

#----------------------------Backend work flow / Game Section-----------------------#
    # Random Chosen Vocabulary , This Part runs in get_question
    def choose_random_vocabulary(self):
        """To choose a random vocabulary from base data
         - ATTENTION this version works just with nested Json files."""
        data = self.base_question_data # Simplify the text form
        key_list = [key for key in data] # Get the Key from Dictionary
        chosen_word = random.choice(key_list) # Use random to choose a word
        self.current_vocabulary.append(chosen_word) # Then just get the values
        self.current_vocabulary.append(data[chosen_word]["german"])
        self.current_vocabulary.append(data[chosen_word]["hiragana"])
        self.current_vocabulary.append(data[chosen_word]["romaji"])
        self.current_vocabulary.append(data[chosen_word]["audio"])

    # Next Question Button
    def get_question(self):
        """This Function is attached to next_question Button"""
        self.current_vocabulary = [] # Clear List before Process next sequence
        temp_unknown = {}
        self.question_de_label.config(text="")
        self.question_rj_label.config(text="")  # Hiragana
        self.answer_hg_label.config(text="")  # Romaji
        self.choose_random_vocabulary()
        data = self.current_vocabulary # Just for simpel it / not to write all the time se...
        print(data) # This is as info for you to see if German is not shown, must change question_label.config number
        self.question_de_label.config(text=data[1]) # German
        # The yes/no question is their for, that user can hand right hiragana ( This is the most important)
        question1 = messagebox.askyesno(message="Write the name in Hiragana on papier\nand press yes, else: no")
        if question1 == True:
            self.play_audio()
            self.question_rj_label.config(text=data[0]) # Romaji
            self.answer_hg_label.config(text=data[2]) # Hiragana
            self.correct_score += 1
            self.score_correct_label.config(text=f"Correct score: {self.correct_score}")
        else:
            self.play_audio()
            self.question_rj_label.config(text=data[0])  # Romaji
            self.answer_hg_label.config(text=data[2])  # Hiragana
            self.wrong_score += 1
            self.score_incorrect_label.config(text=f"wrong score: {self.wrong_score}")
            temp_unknown = {
                "german": data[1],
                "hiragana": data[2],
                "romaji": data[0],
                "audio": data[4]
            }
            self.temp_incorrect_question[data[0]] = temp_unknown # will Add the unknown words to list and be created a log, to track




    # Audio Section Open file and play Audio
    def play_audio(self):
        """Play audio function"""
        try:
            audio = self.current_vocabulary[4] # Audio file path
            pygame.mixer.music.load(audio) # load Audio
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue
        except pygame.error as e:
            print(f"Error playing audio: {e}")
            # self.correct_label.config(text="Audio not found!", fg="red")

    # Log function
    def log_writer(self):
        """Create a Json Log file from unknown vocabulary
        - Save Current unknown Vocabulary to new json file"""
        new_data = self.temp_incorrect_question
        file_path = "./assets/data_base/unknown_jp_vocab.json"
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            old_data.update(new_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(old_data,f,indent=4,ensure_ascii=False)
                print("data saved!!!")
        except FileNotFoundError:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(new_data,f,indent=4,ensure_ascii=False)
                print("data saved!!!")





if __name__=="__main__":
    game = QuestionAndAnswer()
    game.mainloop()