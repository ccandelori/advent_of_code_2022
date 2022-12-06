with open("input") as f:
    signal = f.read()

packet_pos = 0
while packet_pos < len(signal):
    window = signal[packet_pos:packet_pos+4]
    if len(set(window)) == len(window): 
        print(f"position: {packet_pos + 4}, window: {window}, letter at position: {signal[packet_pos + 3]}")
        break
    else:
        packet_pos += 1

msg_pos = packet_pos + 4
while msg_pos < len(signal):
    window = signal[msg_pos:msg_pos + 14]
    if len(set(window)) == len(window): 
        print(f"position: {msg_pos + 14}, window: {window}, letter at position: {signal[msg_pos + 13]}")
        break
    else:
        msg_pos += 1