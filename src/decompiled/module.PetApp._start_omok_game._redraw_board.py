# module.PetApp._start_omok_game._redraw_board
# source line 6667
# Recovered from bytecode; default argument values are not shown.

def _redraw_board(event):
    try:
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
        avail = max(80, min(cw, ch))
        margin = max(10, int(avail * 0.055))
        cell = max(6, (avail - 2 * margin) / (n - 1))
        ctx['margin'] = margin
        ctx['cell'] = cell
        canvas.delete('all')
        line_color = '#999999'
        for i in range(n):
            yline = margin + i * cell
            xline = margin + i * cell
            canvas.create_line(margin, yline, margin + (n - 1) * cell, yline, fill = line_color)
            canvas.create_line(xline, margin, xline, margin + (n - 1) * cell, fill = line_color)
        stone_size = max(6, int(cell * 0.92))
        if ctx.get('stone_size') != stone_size:
            ctx['stone_size'] = stone_size
            ctx['photo'] = {
                'B': self._omok_stone_photo('B', stone_size),
                'A': self._omok_stone_photo('A', stone_size) }
        for yy in range(n):
            for xx in range(n):
                c = ctx['board'][yy][xx]
                if not c:
                    continue
                px = margin + xx * cell
                py = margin + yy * cell
                canvas.create_image(px, py, image = ctx['photo'][c], tags = 'stone')
            range(n)
        None('A')
        None('B')
        return None
    except Exception:
        return None
