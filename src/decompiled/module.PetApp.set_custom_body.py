# module.PetApp.set_custom_body
# source line 4807
# Recovered from bytecode; default argument values are not shown.

def set_custom_body(self, dex):
    if dex is not None:
    
        try:
            pinned_dex = self.starter_stage_conf().get('dex')
            if pinned_dex is not None and int(dex) == int(pinned_dex):
                dex = None
            if dex is None:
                self.state['custom_body_dex'] = None
            else:
                dex = int(dex)
                self._ensure_body_anim_loaded(dex)
                self.state['custom_body_dex'] = dex
                self._remove_dex_from_companion_slots(dex)
            self.save_state()
            self._finish_to_idle()
            self.redraw()
        
            try:
                if self.tray_icon:
                
                    try:
                        self.tray_icon.icon = self._tray_image()
                        return None
                        return None
                        except Exception:
                            pinned_dex = None
                            continue
                    except Exception:
                        return None
