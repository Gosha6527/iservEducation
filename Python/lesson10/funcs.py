from data import *
quest_index = 0
right_answers = 0
quest_data = questions
def generate_quest(quest, buttons):
    if quest_index < len(quest_data):
        quest.config(text=quest_data[quest_index]["quest"])
        print(0)
        for i in range(len(buttons)):
            buttons[i].config(text=quest_data[quest_index]["answers"][i])
    else:
        global right_answers
        quest.config(text=f"Викторина закончена! Вы набрали:{right_answers}")
        for btn in buttons:
            btn.config(state="disabled")

def choice(button, quest, buttons, info):
    global quest_data
    global quest_index
    global right_answers
    if buttons[0]["text"] == quest_data[quest_index]["answers"][0]:
        if button["text"] == quest_data[quest_index]["right"]:
            quest_index += 1
            right_answers += 1
            info.config(text="")
            generate_quest(quest, buttons)
        else:
            if quest_index < len(quest_data):
                t = quest_data[quest_index]["right"]
                quest_index += 1
                info.config(text=f"Ответ неверный, правильный ответ {t},  нажмите любую кнопку чтобы продолжить")
            
    else:
        generate_quest(quest, buttons)
        info.config(text="")
            