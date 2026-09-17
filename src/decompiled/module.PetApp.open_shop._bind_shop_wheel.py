# module.PetApp.open_shop._bind_shop_wheel
# source line 13181
# Recovered from bytecode; default argument values are not shown.

def _bind_shop_wheel(_e):
    outer_canvas.bind_all('<MouseWheel>', _shop_wheel)
    outer_canvas.bind_all('<Button-4>', _shop_wheel)
    outer_canvas.bind_all('<Button-5>', _shop_wheel)
