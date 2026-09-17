# module.PetApp._show_minigame_result_popup
# source line 5544
# Recovered from bytecode; default argument values are not shown.

def _show_minigame_result_popup(self, win, practice, lines, close_fn, retry_fn):
    popup = None(win)
    popup.title('결과')
    popup.resizable(False, False)

    try:
        popup.transient(win)
    
        try:
            popup.attributes('-topmost', True)
            None(popup, text = '🏁 결과', font = ('맑은 고딕', 12, 'bold')).pack(padx = 24, pady = (18, 6))
            for line in lines:
                None(popup, text = line, font = ('맑은 고딕', 10), justify = 'left', wraplength = 260).pack(padx = 20, pady = 1)
            lines
            btn_row = None(popup)
            btn_row.pack(pady = (14, 18))
            popup.update_idletasks()
        
            try:
                ph = popup.winfo_reqheight()
                pw = popup.winfo_reqwidth()
                px = win.winfo_rootx() + max(0, (win.winfo_width() - pw) // 2)
                py = win.winfo_rooty() + max(0, (win.winfo_height() - ph) // 2)
                popup.geometry(f'''{pw}x{ph}+{px}+{py}''')
            
                try:
                    popup.grab_set()
                    return None
                    except Exception:
                        tk.Button
                        continue
                    except Exception:
                        tk.Button
                        continue
                    except Exception:
                        tk.Button
                        continue
                except Exception:
                    tk.Button
                    return None
