# module.PetApp._make_hscroll_row
# source line 8179
# Recovered from bytecode; default argument values are not shown.

def _make_hscroll_row(self, parent, height):
    wrap = None(parent)
    canvas = None(wrap, height = height, highlightthickness = 0)
    hscroll = None(wrap, orient = 'horizontal', command = canvas.xview)
    canvas.configure(xscrollcommand = hscroll.set)
    canvas.pack(side = 'top', fill = 'x', expand = True)
    hscroll.pack(side = 'top', fill = 'x')
    inner = None(canvas)
    canvas.create_window((0, 0), window = inner, anchor = 'nw')

    def _on_inner_configure(evt = None):
        '''all'''
    
        try:
            canvas.configure(scrollregion = canvas.bbox('all'))
            return None
        except Exception:
            return None


    inner.bind('<Configure>', _on_inner_configure)

    def _on_wheel(evt):
        delta = -1 if evt.delta > 0 else 1
    
        try:
            canvas.xview_scroll(delta, 'units')
            return None
        except Exception:
            return None



    def _bind_wheel(evt = None):
        '''<MouseWheel>'''
    
        try:
            canvas.bind_all('<MouseWheel>', _on_wheel)
            return None
        except Exception:
            return None



    def _unbind_wheel(evt = None):
        '''<MouseWheel>'''
    
        try:
            canvas.unbind_all('<MouseWheel>')
            return None
        except Exception:
            return None


    canvas.bind('<Enter>', _bind_wheel)
    canvas.bind('<Leave>', _unbind_wheel)
    canvas.bind('<Destroy>', _unbind_wheel, add = '+')
    return (wrap, inner)
