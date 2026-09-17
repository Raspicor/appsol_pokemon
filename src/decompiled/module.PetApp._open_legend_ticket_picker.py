# module.PetApp._open_legend_ticket_picker
# source line 14642
# Recovered from bytecode; default argument values are not shown.

def _open_legend_ticket_picker(self, gen):
    legends = sorted(LEGENDARY_DEX_BY_GEN.get(gen, []))
    if not legends:
        None('PikaPet', f'''{gen}세대에는 아직 등록된 전설 포켓몬이 없어요.''')
        return None
    win = None(self.root)
    win.title(f'''🎫 {gen}세대 전설 선택권 사용''')
    resolve_species_win(win, 380, 560)

    try:
        win.attributes('-topmost', True)
        bottom = None(win)
        bottom.pack(side = 'bottom', pady = 10)
        body = None(win)
        body.pack(side = 'top', fill = 'both', expand = True, padx = 14, pady = (14, 4))
        None(body, text = '하나만 고를 수 있어요 - 고르는 즉시 Lv.5로 바로 지급돼요!', font = ('맑은 고딕', 9, 'bold'), wraplength = 340, justify = 'left').pack(anchor = 'w', pady = (0, 8))
        state_box = {
            'used': False }
        buttons = []
    
        def _pick(dex):
            '''used'''
            if state_box['used']:
                return None
            state_box['used'] = None
            for b in buttons:
                b.configure(state = tk.DISABLED)
            self._grant_legend_ticket_pokemon(gen, dex)
        
            try:
                win.destroy()
                return None
                except Exception:
                    continue
            except Exception:
                return None


        list_outer = None(body)
        list_outer.pack(fill = 'both', expand = True)
        list_canvas = None(list_outer, highlightthickness = 0)
        list_vsb = None(list_outer, orient = 'vertical', command = list_canvas.yview)
        list_frame = None(list_canvas)
        list_frame.bind('<Configure>', (lambda e: list_canvas.configure(scrollregion = list_canvas.bbox('all'))))
        list_canvas.create_window((0, 0), window = list_frame, anchor = 'nw')
        list_canvas.configure(yscrollcommand = list_vsb.set)
        list_canvas.pack(side = 'left', fill = 'both', expand = True)
        list_vsb.pack(side = 'right', fill = 'y')
    
        def _ticket_wheel(event):
            '''num'''
            delta = -1 if getattr(event, 'num', 0) == 5 or event.delta < 0 else 1
        
            try:
                if list_canvas.winfo_exists():
                
                    try:
                        list_canvas.yview_scroll(-delta, 'units')
                        return None
                        return None
                    except Exception:
                        return None



    
        def _bind_ticket_wheel(_e = None):
            '''<MouseWheel>'''
            list_canvas.bind_all('<MouseWheel>', _ticket_wheel)
            list_canvas.bind_all('<Button-4>', _ticket_wheel)
            list_canvas.bind_all('<Button-5>', _ticket_wheel)

    
        def _unbind_ticket_wheel(_e = None):
            '''<MouseWheel>'''
            list_canvas.unbind_all('<MouseWheel>')
            list_canvas.unbind_all('<Button-4>')
            list_canvas.unbind_all('<Button-5>')

        list_canvas.bind('<Enter>', _bind_ticket_wheel)
        list_canvas.bind('<Leave>', _unbind_ticket_wheel)
        win.bind('<Destroy>', (lambda e: None()), add = '+')
        for dex in legends:
            e = POKEDEX.get(dex, { })
            row = None(list_frame, relief = 'groove', bd = 1)
            row.pack(fill = 'x', pady = 3)
            aset = None(sprite_folder_path(e.get('en')))
            frame = aset.frame(e.get('idle', 'Idle'), 0, spriteanim.DIR_DOWN)
            icon = frame.convert('RGBA') if frame is not None else draw_pokeball_image(48)
            photo = None(icon)
            icon_lbl = None(row, image = photo)
            icon_lbl.image = photo
            icon_lbl.pack(side = 'left', padx = 6, pady = 4)
            btn = None(row, text = f'''{e.get('kr', '?')} 선택하기''', command = (lambda d = dex: None(d)))
            btn.pack(side = 'left', padx = 6)
            buttons.append(btn)
        tk.Label
        None(bottom, text = '취소', command = win.destroy).pack()
        self._add_opacity_control(win)
        return None
    except Exception:
        continue
        except Exception:
            frame = None
            continue
