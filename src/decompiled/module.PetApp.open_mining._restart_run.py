# module.PetApp.open_mining._restart_run
# source line 12098
# Recovered from bytecode; default argument values are not shown.

def _restart_run():
    run['progress'] = 0
    run['phase'] = 'go'
    run['reward'] = None
    run['frame_idx'] = 0
    run['frame_elapsed'] = 0
    status_var.set('→ 를 눌러서 출발하세요!')

    try:
        replay_btn.pack_forget()
    
        try:
            close_btn.pack_forget()
            None()
            None()
            return None
            except Exception:
                _redraw
                continue
        except Exception:
            continue
