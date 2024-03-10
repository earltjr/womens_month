import customtkinter as ctk
from tktooltip import ToolTip
import subprocess
import os

#set appearance, size, color and them of window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root=ctk.CTk()
root.geometry("800x500")
###########################################################################
#creates custom frame 
frame=ctk.CTkFrame(master=root)
frame.pack(pady=60,padx=60,fill="both",expand=True)

#creates label for frame
label=ctk.CTkLabel(master=frame,text="Women's month GUI", font=("Ariel",24))
label.pack(pady=15,padx=10)

#adds a button to the frame and sets its appearance and size settings and creates tool tip for button
button1=ctk.CTkButton(master=frame, text="clean all files starting from step2")
button1.pack(pady=10,padx=10)
button1_msg="This will execute add_professions.py and add_profession_tags.py for women's month data, at least ONE properly formated excel should be located in the step2 folder"
button1.tooltip= ToolTip(button1, msg=button1_msg, delay=0.01, follow=False,
        parent_kwargs={"bg": "gray20", "padx": 3, "pady": 3},
        fg="white", bg="grey", padx=10, pady=10)

# function executes add_profession.py and add_profession_tag.py scripts
def execute_scripts():
    try:
        script_path1=os.path.join(os.path.dirname(__file__),'add_profession.py')
        script_path2=os.path.join(os.path.dirname(__file__),'add_profession_tag.py')
       
        result1 = subprocess.run(['python', script_path1], capture_output=True, text=True)
       

        result2= subprocess.run(['python', script_path2], capture_output=True, text=True)
        
        msg = "Scripts output1: {}\nScripts output2: {}".format(result1.stdout, result2.stdout)
        label_output.configure(text=msg)
        
    except Exception as e:
        print("Error:", e)

button1.configure(command=execute_scripts)

# Output label
label_output = ctk.CTkLabel(master=frame, text="", font=("Arial", 12))
label_output.pack(pady=10, padx=10)


root.mainloop()