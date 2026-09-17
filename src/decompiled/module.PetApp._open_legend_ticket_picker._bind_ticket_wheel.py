# module.PetApp._open_legend_ticket_picker._bind_ticket_wheel
# source line 14707
# Recovered from bytecode; default argument values are not shown.

def _bind_ticket_wheel(_e):
    list_canvas.bind_all('<MouseWheel>', _ticket_wheel)
    list_canvas.bind_all('<Button-4>', _ticket_wheel)
    list_canvas.bind_all('<Button-5>', _ticket_wheel)
