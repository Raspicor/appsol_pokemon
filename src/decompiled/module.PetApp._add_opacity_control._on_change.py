# module.PetApp._add_opacity_control._on_change
# source line 18331
# Recovered from bytecode; default argument values are not shown.

def _on_change(v):
    try:
        pct = int(float(v))
        alpha = max(0.15, min(1, pct / 100))
        self.state['window_opacity'] = alpha
        self.save_state()
        _apply_opacity_to_all_open_windows(alpha)
        return None
    except Exception:
        return None
