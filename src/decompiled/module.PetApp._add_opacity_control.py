# module.PetApp._add_opacity_control
# source line 18318
# Recovered from bytecode; default argument values are not shown.

def _add_opacity_control(self, parent):
    row = None(parent)
    row.pack(side = 'bottom', fill = 'x', padx = 10, pady = (2, 6))
    top_row = None(row)
    top_row.pack(fill = 'x')
    None(top_row, text = '🔆 창 투명도', font = ('맑은 고딕', 8), fg = '#777').pack(side = 'left')
    pct0 = int(round(self.state.get('window_opacity', 1) * 100))

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


    scale = None(top_row, from_ = 15, to = 100, orient = 'horizontal', showvalue = True, length = 110, command = _on_change)
    scale.set(pct0)
    scale.pack(side = 'left', padx = (6, 0))
    None(row, text = "%  (안 보일 땐 트레이 아이콘이나 포켓몬 우클릭 메뉴의 '투명도 복구' 이용)", font = ('맑은 고딕', 7), fg = '#999', wraplength = 260, justify = 'left').pack(anchor = 'w', pady = (2, 0))
    return row
