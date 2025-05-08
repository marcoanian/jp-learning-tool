# Virtual Japanese Keyboard Version 1.0 Author: Marco Anian
#------------------------------DOC---------------------------------#
"""
Virtual Japanese Keyboard Dashboard – Version 1.0
Author: Marco Anian

This tool serves as the main control panel for launching multiple interactive Japanese learning tools.

Modules included:
- Japanese Virtual Keyboard: Input Hiragana characters, convert to Romaji, save and manage custom vocabulary.
- Q&A Game Launcher: A vocabulary-based quiz game with audio playback and score tracking.
- Text-to-Audio Generator: Convert JSON-based vocab into playable Japanese audio files using gTTS.
- Note Pad: Write, import, and export text notes related to learning.

Features:
- Dual-direction vocab dictionaries (Japanese and German)
- GUI-based button input for Hiragana characters
- Modular tool launching (game, converter, data builder)
- Voice integration and JSON export
- CustomTkinter design with modern layout and theme

Designed with love for learning, powered by clarity, and built by Marco Anian.
"""

#---------------------------Imports----------------------------------#
import customtkinter
from customtkinter import CTkTextbox, CTkButton, CTkLabel, CTkEntry, CTkFrame
from tkinter import filedialog, messagebox
import json
from json import JSONDecoder
from text_to_audio_converter import JapaneseTextToAudio
from question_answer_game import QuestionAndAnswer



#-----------------------Constants-------------------------------------#
font_family = "Segoe UI"  # or "Consolas", "Verdana", etc.
FONT = (font_family,10,"normal")
FONT1 = ("courier", 15 ,"bold")
BGC = "#142B3D"
Light_Sky_Blue = "#87CEFA"	#Fresh, clear, energetic


HG_DB_PATH = "assets/raw_data/raw_hg_db.json" # Raw Data Jp
RJ_DB_PATH = "assets/raw_data/raw_romaji_hg_db.json" # Romaji to Hg Data
DATA_CREATED_PATH_JP = "assets/data_base/own_db_create_jp.json"
DATA_CREATED_PATH_LA = "assets/data_base/own_db_create_la.json"
HELP_TXT = """
📚 HOW TO USE THIS TOOL 📚

1. Type Hiragana using the virtual keyboard or manually in the 'Hiragana' field.
2. Press 'Convert to Romaji' to see the Romanized form.
3. Add your vocabulary (Hiragana, Romaji, German meaning) using 'Add to Dict'.
4. View your full dictionary with 'Display Dict' and save it as a JSON file.
5. Use the 'ToA' button to convert your vocab to spoken audio (MP3).
6. Use the note pad to write example sentences or notes. Import/export your notes as text files.
7. Launch the Q&A game with one click to practice what you've learned.

🎌 Notes:
- JSON vocab must follow the nested structure for audio and game integration.
- All your saved words are compatible with the Q&A and audio tools.

Built for learning, and progress.
"""
#-----------------------Class------------------------------------------#

class HiraganaLearningTool(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.audio_converter = JapaneseTextToAudio()
        self.current_data = {} # To Store current data , key hg
        self.current_data_latin = {}
        self.hiragana_db = self.load_main_db_json() # Load Keyboard transl_data
        self.romaji_db = self.load_romaji_db_json()

        # Window properties
        self.title("HiraganaLearningTool V1")
        self.geometry("1250x720")
        self.resizable(False, False)
        self.wm_attributes("-alpha", 0.96)  # Slight transparency
        # Label
        label_frame = CTkFrame(self,width=100, height=50)
        label_frame.place(x=5,y=15)

        hg_label = CTkLabel(label_frame,text="Hiragana",font=FONT).pack(side="left",padx=200,pady=5)
        romaji_label = CTkLabel(label_frame, text="Romaji", font=FONT).pack(side="left",padx=180,pady=5)
        latin_label = CTkLabel(label_frame, text="Latin", font=FONT).pack(side="left",padx=190,pady=5)
        # Entry
        entry_frame = CTkFrame(self)
        entry_frame.place(x=20, y=80)
        self.hg_entry = CTkEntry(entry_frame,font=FONT1,width=350)
        self.hg_entry.pack(side="left",padx=25,pady=5)
        self.rj_entry = CTkEntry(entry_frame, font=FONT1, width=350)
        self.rj_entry.pack(side="left",padx=25, pady=5)
        self.latin_entry = CTkEntry(entry_frame, font=FONT1, width=350)
        self.latin_entry.pack(side="left", padx=25, pady=5)

        # Text Entry
        self.text_box = CTkTextbox(self,width=500,height=400,font=FONT1,wrap="word")
        self.text_box.insert("1.0",f"Note pad, to save your notes, can be exported to txt or imported\n{HELP_TXT}")
        self.text_box.place(x=650,y=200)
        # Btn for Text box
        import_txt_btn = CTkButton(self, text="Import from txt", bg_color=BGC, text_color="white", fg_color="dark Green",command=self.import_txt)
        import_txt_btn.place(x=650, y=650)
        save_txt_btn = CTkButton(self, text="Export to txt", bg_color=BGC, text_color="white", fg_color="dark Green",command=self.export_notes)
        save_txt_btn.place(x=850, y=650)
        clear_btn = CTkButton(self, text="Clear Text", bg_color=BGC, text_color="white", fg_color="dark red",command=self.clear_text_box_func)
        clear_btn.place(x=1050, y=650)

        conv_text_to_audio_btn = CTkButton(self, text="ToA", bg_color=BGC, text_color="white", fg_color="dark red",width=10,height=12,
                              command=self.toa_pipeline)
        conv_text_to_audio_btn.place(x=1180, y=400)

        # Hiragana Buttons
        button_frame = CTkFrame(self)
        button_frame.place(x=20, y=200)

        # Hiragana Characters
        char = ['あ', 'い', 'う', 'え', 'お', " ", ",", "@", ".", "?", "!",
                'か', 'き', 'く', 'け', 'こ', " ", 'が', 'ぎ', 'ぐ', 'げ', 'ご',
                'さ', 'し', 'す', 'せ', 'そ', " ", 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
                'た', 'ち', 'つ', 'て', 'と', " ", 'だ', 'ぢ', 'づ', 'で', 'ど',
                'な', 'に', 'ぬ', 'ね', 'の', " ", 'ん', " ", " ", " ", " ",
                'は', 'ひ', 'ふ', 'へ', 'ほ', " ", 'ば', 'び', 'ぶ', 'べ', 'ぼ',
                'ま', 'み', 'む', 'め', 'も', " ", 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
                'ら', 'り', 'る', 'れ', 'ろ', "/ ", "-", "=", "三", "四", "五",
                'や', 'ゆ', 'よ', 'わ', 'を', " = > ", "六", "七", "八", "九", "0"
                ]
        # Create Buttons in a Grid Layout
        row = 0
        col = 0
        for idx, item in enumerate(char):
            self.button = CTkButton(
                button_frame,
                text=f"{item}",
                width=40,
                height=40,
                bg_color="#142B3D",
                font=FONT1,
                command=lambda item=item: self.command_button(item)  # Pass button text to the method
            )
            self.button.grid(row=row, column=col, padx=5, pady=5)  # Use grid to place buttons within the frame
            col += 1
            if col > 10:  # Adjust number of buttons per row
                col = 0
                row += 1

        # Execute Buttons
        convert_btn = CTkButton(self,text="Convert to romaji",bg_color=BGC,command=self.convert_to_romaji)
        convert_btn.place(x=20,y=150)
        add_to_dic_btn = CTkButton(self, text="Add to Dict", bg_color=BGC,command=self.add_to_dict_funct)
        add_to_dic_btn.place(x=200, y=150)
        clear_btn = CTkButton(self, text="Clear fields", bg_color=BGC,text_color="white",fg_color="dark red",command=self.clear_btn_func)
        clear_btn.place(x=380, y=150)
        show_dict_btn = CTkButton(self, text="Display Dict", bg_color=BGC,text_color="white",fg_color="Green",command=self.show_dict_function)
        show_dict_btn.place(x=560, y=150)
        save_dict_btn = CTkButton(self, text="Save to Json", bg_color=BGC, text_color="white", fg_color="dark Green",command=self.save_to_json)
        save_dict_btn.place(x=740, y=150)
        help_btn = CTkButton(self, text="Help", bg_color=BGC, text_color="white", fg_color="gray",command=self.help_function)
        help_btn.place(x=920, y=150)
        lunch_game_btn = CTkButton(self, text="Q&A Game", bg_color=BGC, text_color="Dark red", fg_color="white",command=self.launch_game)
        lunch_game_btn.place(x=1100, y=150)

#----------------------------Method / Functions----------------------#
    # Main Button Functions
    def command_button(self, text):
        """Handle button click."""
        print(f"Button clicked: {text}")  # Prints the text of the button
        self.hg_entry.insert("end", text)  # Add the button text to the display

    def clear_btn_func(self):
        """Clear all Entry fields"""
        self.hg_entry.delete(0,"end")
        self.rj_entry.delete(0,"end")
        self.latin_entry.delete(0,"end")

    def clear_text_box_func(self):
        """Clear Text Box"""
        self.text_box.delete("1.0","end")

    def show_dict_function(self):
        """Display current Dit's in Text box"""
        data = self.current_data
        latin_data = self.current_data_latin
        formated_jp = ""
        formated_latin = ""
        for key, value in data.items():
            formated_jp += f"{key} | romaji: {value["romaji"]} | latin: {value["german"]}\n"
        for key, value in latin_data.items():
            formated_latin += f"{key} | romaji: {value["romaji"]} | hiragana: {value["hiragana"]}\n"
        self.text_box.insert("end",f"{formated_jp}\n{formated_latin}")

    def help_function(self):
        """Show the Help text / How to use"""
        messagebox.showinfo(title="Help / How to use", message=HELP_TXT)

    def convert_to_romaji(self):
        """Convert Hiragana to Romaji."""
        hg_data = self.hg_entry.get().strip()
        temp_romaji_word = "" # To save current letter and final word
        for letter in hg_data:
            if letter in self.hiragana_db.keys():
                word = self.hiragana_db.get(letter)
                temp_romaji_word += word
        self.rj_entry.insert("end",temp_romaji_word)

    def save_to_json(self):
        """Get Current database:
        - Convert it to audio, create dict with audio path
        - return dict"""
        self.save_update_to_json_jp()
        self.save_update_to_json_la()

    # Backend operations Functions #
    def load_main_db_json(self):
        """Load Hiragana Database.
        backend operation"""
        try:
            with open(HG_DB_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except (Exception, FileNotFoundError) as e:
            messagebox.showerror(title="Error Window Load Database", message=f"{e}\nCheck directory")

    def load_romaji_db_json(self):
        """Load Hiragana Database.
        backend operation"""
        try:
            with open(RJ_DB_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except (Exception, FileNotFoundError) as e:
            messagebox.showerror(title="Error Window Load Database", message=f"{e}\nCheck directory")



    def add_to_dict_funct(self):
        """Create a nested Dictionary.
        Latin = in my case is German"""
        temp_file_jp = {}
        temp_file_latin = {}
        key = self.hg_entry.get()
        romaji = self.rj_entry.get()
        latin = self.latin_entry.get()
        # To Create a Japanese Key Dict
        temp_file_jp[key] = {"hiragana":key,"romaji":romaji,"german":latin}
        self.current_data.update(temp_file_jp)
        # To Create a Latin based Dict
        temp_file_latin[latin] =  {"hiragana":key,"romaji":romaji,"german":latin}
        self.current_data_latin.update(temp_file_latin)
        self.clear_btn_func()

    def save_update_to_json_jp(self):
        """Write / Update own create databased, backend operation"""
        new_data_jp = self.current_data
        convert_data_to_audio = self.audio_converter.audio_generator_nested_file(new_data_jp)
        file_path = filedialog.askopenfilename(title="update json file",defaultextension="*.json")
        try:
            with open(file_path,"r", encoding="utf-8") as f:
                old_data = json.load(f)
            old_data.update(convert_data_to_audio)
            save_to = filedialog.asksaveasfilename(title="Save update json file",defaultextension="*.json")
            with open(save_to, "w",encoding="utf-8") as f:
                json.dump(old_data,f,indent=4,ensure_ascii=False)
        except (Exception,FileNotFoundError,JSONDecoder) as e:
            print(e)
            save_to = filedialog.asksaveasfilename(title="Save update json file", defaultextension="*.json")
            with open(save_to, "w",encoding="utf-8") as f:
                json.dump(convert_data_to_audio,f,indent=4,ensure_ascii=False)

    def save_update_to_json_la(self):
        """Write / Update own create databased, backend operation"""
        new_data_la = self.current_data_latin
        try:
            with open(DATA_CREATED_PATH_LA,"r", encoding="utf-8") as f:
                old_data = json.load(f)
            old_data.update(new_data_la)
            with open(DATA_CREATED_PATH_JP, "w",encoding="utf-8") as f:
                json.dump(old_data,f,indent=4,ensure_ascii=False)
        except (Exception,FileNotFoundError,JSONDecoder) as e:
            print(e)
            with open(DATA_CREATED_PATH_JP, "w",encoding="utf-8") as f:
                json.dump(new_data_la,f,indent=4,ensure_ascii=False)

    def import_txt(self):
        file_path = filedialog.askopenfilename(title="open txt file", defaultextension="*.txt")
        try:
            with open(file_path,"r", encoding="utf-8") as f:
                old_data = f.read()
            for line in old_data:
                formated_text = f"{line}\n"
                self.text_box.insert("end",formated_text)
        except Exception as e:
            print(e)
            return "Something went wrong!!"

    def export_notes(self):
        data = self.text_box.get("1.0","end")
        save_to = filedialog.asksaveasfilename(title="Save update json file", defaultextension="*.json")
        try:
            with open(save_to, "w", encoding="utf-8") as f:
                f.write(data)
                print("data saved!!!")
        except Exception as e:
            print(e)

    def launch_game(self):
        qa_game = QuestionAndAnswer()
        qa_game.mainloop()

    def toa_pipeline(self):
        self.audio_converter.pipeline_converter_from_json()





if __name__=="__main__":
    h_tool = HiraganaLearningTool()
    h_tool.mainloop()
