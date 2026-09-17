# module.PetApp.open_shop._food_tick
# source line 13340
# Recovered from bytecode; default argument values are not shown.

def _food_tick():
    try:
        if not win.winfo_exists():
            return None
        bl = time.time - None()
        if bl > 0:
            _food_tick_state['was_active'] = True
            blt = int(bl)
            mm = ()
            ss = divmod(blt, 60)
        
            try:
                food_btn.configure(text = f'''🍎 사용 중! (조우확률 2배, {mm}분 {ss:02d}초 남음)''')
            if _food_tick_state['was_active']:
                None()

        win.after(1000, _food_tick)
        return None
    except Exception:
        return None
        except Exception:
            continue
