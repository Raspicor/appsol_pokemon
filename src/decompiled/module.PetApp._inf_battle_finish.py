# module.PetApp._inf_battle_finish
# source line 14506
# Recovered from bytecode; default argument values are not shown.

def _inf_battle_finish(self, gctx, won, conceded):
    flags = gctx['flags']
    if flags['ended']:
        return None
    flags['ended'] = None
    flags['locked'] = True
    win = gctx['win']
    mode = gctx['inf_mode']
    stage = gctx['inf_stage']
    if not won:
    
        try:
            self._inf_win_pos = (win.winfo_x(), win.winfo_y())
        
            try:
                win.destroy()
                if not conceded:
                    None('PikaPet', f'''스테이지 {stage}에서 졌어요... 스테이지는 그대로예요. HP를 회복하고 다시 도전해보세요!\n(진 건 아무 불이익이 없어요)''')
                return None
                gold = inf_stage_gold(stage)
                gold_title_msgs = self._earn_gold(gold)
                msgs = [
                    f'''🎉 스테이지 {stage} 클리어! 💰{gold}골드 획득!''']
                cycle = ()
                gen = inf_stage_cycle_info(stage)
                pos_in_block = messagebox.showinfo
                _pos_in_cycle = None
                if stage % INF_FREE_GACHA_EVERY == 0 and grant_msg:
                    msgs.append(grant_msg)
                if kind == 'mirror':
                    self._grant_legend_ticket(next_gen)
                    msgs.append(f'''🎫 {next_gen}세대 전설 선택권을 받았어요! (상점의 \'전설 선택권\' 칸에서 쓸 수 있어요)''')
                stage + 1 = gen + 1 if gen < 4 else 1
                self.state.setdefault('inf_meter_stage', { })[mode] = new_stage
                best = self.state.setdefault('inf_meter_best', { })
                if stage > int(best.get(mode, 0)):
                    best[mode] = stage
                title_msgs = self._check_inf_recurring_title(stage)
                msgs.extend(title_msgs)
                msgs.extend(self._check_gen_master_titles())
                msgs.extend(self._check_new_titles())
                for m in gold_title_msgs:
                    if not m not in msgs:
                        continue
                    msgs.append(m)
                inf_stage_kind(pos_in_block)
                self.save_state()
                if stage >= INF_STAGE_CAP:
                
                    try:
                        self._inf_win_pos = (win.winfo_x(), win.winfo_y())
                    
                        try:
                            win.destroy()
                            None('PikaPet', '\n'.join(msgs) + f'''\n\n🎊 {INF_STAGE_CAP}스테이지 돌파를 축하합니다!\n지금은 여기까지가 끝이에요 - 이후 스테이지는 업데이트 예정입니다. 조금만 기다려주세요!''')
                            return None
                            reward_text = '\n'.join(msgs)
                            self.root.after(50, (lambda : self._start_inf_stage(mode, reward_msg = reward_text, reuse_win = win)))
                            return None
                            except Exception:
                                self._inf_free_gacha_grant(gen)
                                continue
                            except Exception:
                                self._inf_free_gacha_grant(gen)
                                continue
                            except Exception:
                                self._inf_free_gacha_grant(gen)
                                continue
                        except Exception:
                            continue
