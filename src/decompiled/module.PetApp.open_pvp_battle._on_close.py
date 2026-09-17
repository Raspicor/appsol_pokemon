# module.PetApp.open_pvp_battle._on_close
# source line 18146
# Recovered from bytecode; default argument values are not shown.

def _on_close():
    if not b['ended']:
    
        try:
            client.send({
                'type': 'surrender' })
        
            try:
                client.close()
                win.destroy()
                return None
                except Exception:
                    continue
            except Exception:
                continue
