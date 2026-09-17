# module.PetApp.open_todo._toggle_alarm_ui
# source line 18590
# Recovered from bytecode; default argument values are not shown.

def _toggle_alarm_ui(*_a):
    if alarm_on_var.get():
        alarm_detail_row.pack(fill = 'x')
        dur_row.pack(fill = 'x', pady = (2, 0))
        return None
    None.pack_forget()
    dur_row.pack_forget()
