def C_trans_to_E(string):
    C_pun = u'，。！？【】（）《》“‘：；［］｛｝&，．？（）＼％－＋'
    E_pun = u',.!?[]()<>"\':;[]{}&,.?()\\%-+'
    table = {ord(f): ord(t) for f, t in zip(C_pun, E_pun)}
    s = string.translate(table)
    s = s.replace(' ', '')
    s = s.lower()
    s = s.strip()
    return s

