def process_event(event):
  print("The process_event function was called.")

my_button = tk.Button(window, text="Example")
my_button.bind("<Enter>", process_event)