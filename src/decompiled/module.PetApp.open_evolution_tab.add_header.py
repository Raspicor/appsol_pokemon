# module.PetApp.open_evolution_tab.add_header
# source line 8306
# Recovered from bytecode; default argument values are not shown.

def add_header(text):
    rows.append((None, None))
    listbox.insert('end', text)
    listbox.itemconfig('end', fg = '#888')
