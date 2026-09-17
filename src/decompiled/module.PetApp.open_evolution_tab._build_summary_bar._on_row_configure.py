# module.PetApp.open_evolution_tab._build_summary_bar._on_row_configure
# source line 8883
# Recovered from bytecode; default argument values are not shown.

def _on_row_configure(evt):
    row_canvas.configure(scrollregion = row_canvas.bbox('all'), height = max(92, row.winfo_reqheight()))
