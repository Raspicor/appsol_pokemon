# module.PetApp.open_minigame_hub._bind_hub_wheel
# source line 5642
# Recovered from bytecode; default argument values are not shown.

def _bind_hub_wheel(_e):
    hub_canvas.bind_all('<MouseWheel>', _hub_mousewheel)
    hub_canvas.bind_all('<Button-4>', _hub_mousewheel)
    hub_canvas.bind_all('<Button-5>', _hub_mousewheel)
