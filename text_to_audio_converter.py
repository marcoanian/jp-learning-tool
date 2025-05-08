# Text to Audio Tool
#--------------------------Doc---------------------------#
"""This tool converts text to speach
- Convert text to speach
- Save Hiragana, romaji, Your language , audio path
for other points of json: use this:
import string

if word.strip() and word not in string.punctuation:
    # safe to generate audio
or this one:
ignore_list = [" ", ",", ".", "!", "?", "ー", "〜"]
if word not in ignore_list:
    # proceed
"""
#------------------------Imports--------------------------#
import sys
from json import JSONDecodeError, JSONDecoder
import json
from gtts import gTTS
import os
from tkinter import filedialog
#---------------------Constants--------------------------#
audio_save_path = r"D:\python_multi_section_code\Japanese_python_tools\jp_learning_tool_new_version\assets\audio\mix_vocab/"

# Optional: force all paths to use forward slashes
audio_save = audio_save_path.replace("\\", "/")
print(audio_save)

#------------------------Class----------------------------#

class JapaneseTextToAudio:



    def open_text_data(self): # To open main data, just needed if source is json
        """To open data"""
        file_path = filedialog.askopenfilename(title="Open Dataset to Convert",defaultextension="*.json")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                print("data loaded! ") # fdb
                return data
        except (FileNotFoundError, JSONDecodeError) as e:
            print(f"{e}, check directory !!!")
            return {}

    def audio_generator_nested_json(self, data):
        """This function is only for nested json file"""
        new_data = {}
        data_to_convert = data
        for word,details in data_to_convert.items():
            temp_folder = {} # Temp_folder for converting
            jp_text = details["hiragana"]
            audio_save_to = f"{audio_save}{word}.mp3"
            print(audio_save_to)
            tts = gTTS(text=jp_text,lang="ja") # init gtts
            tts.save(audio_save_to)
            details["audio"] = audio_save_to # Add to json
            temp_folder = {
                "german": details["german"],
                "romaji": details["romaji"],
                "hiragana": jp_text,
                "audio": details["audio"]
            }
            print(temp_folder) # fdb
            new_data[details["romaji"]] = temp_folder
        print(new_data) # fdb
        new_file = filedialog.asksaveasfilename(title="Save Json Audio", defaultextension="*.json")
        new_file = new_file.replace("\\", "/")
        with open(new_file, "w", encoding="utf_8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
            print("Audio files created and JSON updated!")

    def audio_generator_nested_file(self, data):
        """This function is only for nested json file"""
        new_data = {}
        data_to_convert = data
        for word,details in data_to_convert.items():
            temp_folder = {} # Temp_folder for converting
            jp_text = details["hiragana"]
            audio_save_to = f"{audio_save}{word}.mp3"
            print(audio_save_to)
            tts = gTTS(text=jp_text,lang="ja") # init gtts
            tts.save(audio_save_to)
            details["audio"] = audio_save_to # Add to json
            temp_folder = {
                "german": details["german"],
                "romaji": details["romaji"],
                "hiragana": jp_text,
                "audio": details["audio"]
            }
            print(temp_folder) # fdb
            new_data[details["romaji"]] = temp_folder
        print(new_data) # fdb
        return new_data



    def single_key_generator(self, audio_data):
        data = audio_data
        new_data = {}

        for key in data:
            word = key.strip()
            if not word:  # Skip empty keys
                continue

            try:
                audio_save_to = f"{audio_save}{word}.mp3"
                tts = gTTS(text=word, lang="ja")
                tts.save(audio_save_to)

                temp_folder = {
                    "hiragana": word,
                    "romaji": data[word],
                    "audio": audio_save_to
                }

                new_data[word] = temp_folder

            except Exception as e:
                print(f"Error with word '{word}': {e}")

        # Save data to JSON
        print(new_data)  # fdb
        new_file = filedialog.asksaveasfilename(title="Save Json Audio", defaultextension="*.json")
        try:
            with open(new_file, "w", encoding="utf_8") as f:
                json.dump(new_data, f, ensure_ascii=False, indent=4)
                print("Audio files created and JSON updated!")
        except JSONDecodeError as e:
            print(f"{e}!!!!")


    def pipeline_converter_from_json(self):
        """This pipeline is for gui. from unknown source
        - Must be nested json file.
        Nested style keys: Hg , Romaji, German/ other lang"""
        data = self.open_text_data()
        self.audio_generator_nested_json(data)
        print("Data Saved!!!")


if __name__=="__main__":
    x = JapaneseTextToAudio()
    data = x.open_text_data()
    #audio = x.single_key_generator(data)
    audio = x.audio_generator_nested_json(data)
    print("everything done!!!")





