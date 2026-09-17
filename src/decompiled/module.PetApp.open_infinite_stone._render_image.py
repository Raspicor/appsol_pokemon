# module.PetApp.open_infinite_stone._render_image
# source line 5832
# Recovered from bytecode; default argument values are not shown.

def _render_image():
    img = load_infinite_stone_image(state_holder['broken'], target_h = size_var.get(), grayscale = color_var.get() == 'gray')
    tkimg = None(img)
    img_label.image = tkimg
    img_label.configure(image = tkimg)
