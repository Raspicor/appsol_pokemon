# module.show_starter_select
# source line 4015
# Recovered from bytecode; default argument values are not shown.

def show_starter_select(root, on_selected):
    root.title('PikaPet - 시작할 포켓몬 고르기')
    root.geometry('860x380')
    root.configure(bg = '#f4f4f4')
    root.resizable(False, False)
    None(root, text = '함께 키울 포켓몬을 하나 골라주세요!', font = ('맑은 고딕', 15, 'bold'), bg = '#f4f4f4').pack(pady = (18, 4))
    None(root, text = '시간이 지나거나 잘 놀아주면 진화해요. 야생 포켓몬을 잡아 도감도 채울 수 있어요.', font = ('맑은 고딕', 9), bg = '#f4f4f4', fg = '#666').pack(pady = (0, 12))
    row = None(root, bg = '#f4f4f4')
    row.pack()
    starters = [
        ('pikachu', '피카츄'),
        ('charmander', '파이리'),
        ('bulbasaur', '이상해씨'),
        ('squirtle', '꼬부기'),
        ('eevee', '이브이')]
    previews = []
    for None in starters:
        key = ()
        kr = None
        None = None(row, bg = '#f4f4f4')
        aset = None(sprite_folder_path(key))
        None(col, text = kr, font = ('맑은 고딕', 11, 'bold'), bg = '#f4f4f4').pack(pady = (8, 4))
        None(col, text = '이 아이로 시작', width = 14, command = (lambda k = key: None(k))).pack()
    tk.Label

    def _on_close():
        for p in previews:
            p.stop()
        root.quit()

    root.protocol('WM_DELETE_WINDOW', _on_close)
    return None
    except Exception:
        tk.Frame
        aset = None
        continue
