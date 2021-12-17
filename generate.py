import binascii

# adjust the range
h_hs = 0xf3
h_he = 0xf4
h_ls = 0x80
h_le = 0xbf

fp = open('output.txt', 'w', encoding='utf-8')

for hex_byte01 in range(h_hs, h_he + 1):
    hex_num01 = hex_byte01+0 << 8
    for hex_byte02 in range(h_ls, h_le + 1):
        hex_num02 = hex_num01+hex_byte02 << 8
        for hex_byte03 in range(h_ls, h_le + 1):
            hex_num03 = hex_num02+hex_byte03 << 8
            fp.write(hex(hex_num03+h_ls) + ' to ' + hex(hex_num03+h_le) + '\n')
            line_var = 0
            space_var = 0
            for hex_byte04 in range(h_ls, h_le + 1):
                if space_var == 5:
                    fp.write(' ')
                    space_var = 0
                if line_var == 16:
                    fp.write('\n')
                    line_var = 0
                    space_var = 0
                hex_num04 = hex_num03+hex_byte04
                num_str = hex(hex_num04)[2:].encode('utf-8')
                try:
                    num_ch = binascii.unhexlify(num_str).decode('utf-8')
                except UnicodeDecodeError:
                    num_ch = '*'
                finally:
                    fp.write(num_ch)
                line_var += 1
                space_var += 1
            fp.write('\n')
fp.close()