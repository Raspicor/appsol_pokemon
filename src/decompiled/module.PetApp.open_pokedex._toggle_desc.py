# module.PetApp.open_pokedex._toggle_desc
# source line 16069
# Recovered from bytecode; default argument values are not shown.

def _toggle_desc():
    desc_visible['v'] = not desc_visible['v']
    if desc_visible['v']:
        desc_label.pack(pady = (2, 6))
        desc_btn.configure(text = '📖 설명 접기 ▲')
        return None
    None.pack_forget()
    desc_btn.configure(text = '📖 설명 보기 ▼')
