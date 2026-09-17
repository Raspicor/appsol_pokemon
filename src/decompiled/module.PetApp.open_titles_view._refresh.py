# module.PetApp.open_titles_view._refresh
# source line 15088
# Recovered from bytecode; default argument values are not shown.

def _refresh():
    for w in body.winfo_children():
        w.destroy()
    if tab_var.get() == 'equip':
        equip_tab_btn.configure(relief = 'sunken', bg = '#dbe7ff')
        list_tab_btn.configure(relief = 'raised', bg = 'SystemButtonFace')
        None()
        return None
    None.configure(relief = 'sunken', bg = '#dbe7ff')
    equip_tab_btn.configure(relief = 'raised', bg = 'SystemButtonFace')
    None()
