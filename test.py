import tkinter as tk
import threading

from chat import send_msg, read_msgs

MSG_HEIGHT = 2
PAD = 2
MAX_LABEL = 10

msg_label_list = []

def init_frames(root):
    
    frame_main_field = tk.Frame(root)
    frame_main_field.pack(fill=tk.BOTH, expand=True)
    frame_msg = tk.Frame (frame_main_field)
    frame_msg.pack(side=tk.RIGHT)
    frame_input = tk.Frame(root)
    frame_input.pack(fill=tk.X, side=tk.BOTTOM)
    label_greet = tk.Label(
        frame_main_field,
        height = MSG_HEIGHT,
        text = 'Chat started...')
    label_greet.pack(side=tk.TOP)
    return frame_msg, frame_input

def init_input_frame(frame):
    txt_entry = tk.Entry(frame)
    label = tk.Label(text = "Nickname")
    name_entry = tk.Entry()
    name_entry.insert(0, 'Anonymous')

    def click(txt_entry):
        txt = txt_entry.get()
        # add_label(txt)
        msg = {'user': name_entry.get(),
               'text': txt
               }
        send_msg(msg)
        txt_entry.delete(0, tk.END)
        # print('Meow!!')

    button = tk.Button(frame,
                       text="Send", 
                       command= lambda: click(txt_entry))
    txt_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)
    button.pack(side=tk.LEFT)
    label.pack(side=tk.LEFT)
    name_entry.pack(side=tk.LEFT)

def add_label(text):
    label = tk.Label(frame_msg,
                    height=MSG_HEIGHT,
                    background='#92c2f2',
                    text=text)
    label.pack(side=tk.TOP,
               anchor=tk.NE,
               padx=PAD,
               pady=PAD)
    msg_label_list.append(label)
    if len(msg_label_list) > MAX_LABEL:
        label_to_del = msg_label_list.pop(0)
        label_to_del.destroy()

def init_gui():
    root = tk.Tk()
    frame_msg, frame_input = init_frames(root)

    init_input_frame(frame_input)
    return root, frame_msg, frame_input

if __name__ == '__main__':
    root, frame_msg, frame_input = init_gui()
    chat_t = threading.Thread(target=read_msgs, args=(add_label,))
    chat_t.start()
    root.mainloop()