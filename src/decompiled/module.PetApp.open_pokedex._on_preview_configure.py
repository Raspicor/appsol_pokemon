# module.PetApp.open_pokedex._on_preview_configure
# source line 16019
# Recovered from bytecode; default argument values are not shown.

def _on_preview_configure(evt):
    preview_canvas.configure(scrollregion = preview_canvas.bbox('all'), width = preview_frame.winfo_reqwidth(), height = preview_frame.winfo_reqheight())
