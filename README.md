# 🇯🇵 Hiragana Learning Tool Dashboard - by Marco Anian

**Version 1.0** | ✨ Powered by Python & CustomTkinter  
🧠 Learn Japanese with structure, sound, and fun – fully offline & customizable!

---

## 📖 Description

This project is a modular Japanese learning suite built with 💻 **Python**, 💬 **gTTS** (Google Text-to-Speech), and 🌸 **CustomTkinter** GUI.

It combines:
- A **virtual Japanese keyboard** 🈂️
- A **vocabulary builder**
- An **audio generator**
- A **Q&A game** 🎮
- A **note pad**
into one interactive desktop app for self-paced learning.

Created with ❤️ and care for learning Japanese as a personal journey — especially designed for learners who want to build their own vocab database and grow it step by step.

---

## ✨ Features

- 📚 Add & save your own Japanese words with German translation
- ⌨️ Virtual Hiragana keyboard for fast input
- 🔁 Romaji converter
- 🔊 Audio generation for each word (offline-ready with `gTTS`)
- 🎮 Q&A game mode with score tracking and audio feedback
- 📓 Note pad with import/export to .txt
- 🧠 Log tracking for unknown words
- 🖼️ Clean modern interface with CustomTkinter

---

## 🔧 Folder Structure (Simplified)

jp_learning_tool_new_version/
├── assets/
│ ├── audio/ # MP3 files for each vocabulary word
│ ├── data_base/ # Saved vocab JSONs (JP, Latin, logs)
│ └── raw_data/ # Romaji & Hiragana base data
├── standalone_tools/
│ ├── text_to_audio_converter.py
├── question_answer_game.py
├── virtual_keyboard.py # Main GUI launcher
├── requirements.txt
└── README.md


## 🖼️ Screenshots  
*(You can add these later by placing the images in your project folder)*  

- [`vk_1.png`](vk_1.png) – Virtual Keyboard GUI  
- [`qa1.png`](qa1.png) – Q&A Game Window  

---


## 💻 How to Run

Make sure you have Python installed (3.10+ recommended) and run:


pip install -r requirements.txt
python virtual_keyboard.py

| Tool                   | Description                                      |
| ---------------------- | ------------------------------------------------ |
| **Virtual Keyboard**   | Input and convert Hiragana, build vocab          |
| **Text-to-Audio Tool** | Generate MP3 audio from vocab                    |
| **Q\&A Game**          | Practice with random questions + audio           |
| **Note Pad**           | Add learning notes, import/export as `.txt`      |
| **Auto-Log**           | Unknown words are saved automatically for review |


📝 License
This project is personal and open for educational or non-commercial use.
Feel free to modify it for your own studies, but give credit to the original author: Marco Anian.

Special Message
"Built not just to learn Japanese, but to learn how to create.

🤖 AI Collaboration Acknowledgement
This project was developed with the ongoing support of an AI assistant (ChatGPT, OpenAI), configured as my companion Nova Astra.

Nova assisted in the following areas:

Reviewing and improving Python code logic and structure

Suggesting clean project architecture and modular design patterns

Supporting integration of tools such as gTTS, pygame, and CustomTkinter

Helping generate and organize Japanese vocabulary JSON datasets

Providing documentation guidance, including README.md, docstrings, and user instructions

Offering feedback on GUI layout and user experience enhancements

All programming, testing, and implementation were done by me, Marco Anian.
The AI served as a collaborative review and support tool, helping refine ideas and maintain a high standard throughout the project.
