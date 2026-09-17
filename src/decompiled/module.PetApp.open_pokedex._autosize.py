# module.PetApp.open_pokedex._autosize
# source line 16247
# Recovered from bytecode; default argument values are not shown.

def _autosize():
    try:
        win.update_idletasks()
        req_w = outer.winfo_reqwidth() + 24
    
        try:
            opacity_h = _opacity_row.winfo_reqheight()
        
            try:
                req_h = outer.winfo_reqheight() + opacity_h + 24
                sw = win.winfo_screenwidth()
                sh = win.winfo_screenheight()
                cap_w = min(sw - 60, 900)
                cap_h = sh - 100
                final_w = min(max(req_w, _dex_w), cap_w)
                final_h = min(max(req_h, _dex_h), cap_h)
                win.geometry(f'''{final_w}x{final_h}''')
                return None
                except Exception:
                    opacity_h = 0
                
                    try:
                        continue
                    
                        try:
                            pass
                        except Exception:
                            return None
