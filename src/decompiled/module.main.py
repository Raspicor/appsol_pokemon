# module.main
# source line 19042
# Recovered from bytecode; default argument values are not shown.

def main():
    try:
        None()
        if not None():
        
            try:
                root = None()
                root.withdraw()
                None('PikaPet', 'PikaPet이 이미 실행 중이에요!\n작업표시줄 오른쪽 트레이 아이콘을 확인해보세요.')
                root.destroy()
                return None
                state = load_state()
                phase = 'pet' if state.get('starter') else 'select'
                if phase == 'select':
                    root = None()
                    result = {
                        'name': None }
                
                    def _pick(name, root = root, result = result):
                        '''name'''
                        result['name'] = name
                        root.quit()

                    show_starter_select(root, _pick)
                    root.mainloop()
                
                    try:
                        root.destroy()
                        if not result['name']:
                            return None
                        state = tk.Tk(DEFAULT_STATE)
                        state['element_train'] = dict(DEFAULT_STATE['element_train'])
                        state['daily_action_count'] = dict(DEFAULT_STATE['daily_action_count'])
                        state['train_sessions'] = dict(DEFAULT_STATE['train_sessions'])
                        state['minigame_daily'] = dict(DEFAULT_STATE['minigame_daily'])
                        state['dex'] = { }
                        state['caught'] = { }
                        state['missed'] = { }
                        state['party'] = []
                        state['catch_counts'] = dict(DEFAULT_STATE['catch_counts'])
                        state['todos'] = []
                        state['starter'] = result['name']
                        state['last_interact_time'] = None()
                        state['stage_started_at'] = None()
                        save_state_to_disk(state)
                        phase = 'pet'
                        continue
                        root = None()
                        _install_error_popup(root)
                        setup_pet_window(root)
                        app = PetApp(root, state)
                        root.protocol('WM_DELETE_WINDOW', app.quit_app)
                        root.mainloop()
                    
                        try:
                            root.destroy()
                            if app.restart_requested:
                                state = load_state()
                                phase = 'select'
                                continue
                            return None
                            except Exception:
                                time.time
                                continue
                            except Exception:
                                time.time
                                return None
                            except Exception:
                                time.time
                                continue
                        except Exception:
                            time.time
                            continue
