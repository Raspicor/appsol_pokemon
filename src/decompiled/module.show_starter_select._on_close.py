# module.show_starter_select._on_close
# source line 4053
# Recovered from bytecode; default argument values are not shown.

def _on_close():
    for p in previews:
        p.stop()
    root.quit()
