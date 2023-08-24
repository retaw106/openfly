import os


def main():
    src_path = './openfly_reverse.dict.yaml'
    dst_path = './openfly_reverse_new.dict.yaml'
    header_line = 11

    header_str = ''
    spell_dict = {}
    with open(src_path, 'r', encoding='utf-8') as f:
        for i in range(header_line):
            line = f.readline()
            header_str += line
        
        line = f.readline()
        while line:
            line_splits = line.split()
            word = line_splits[0]
            spell = line_splits[1]
            if word in spell_dict:
                if spell not in spell_dict[word]:
                    spell_dict[word].append(spell)
            else:
                spell_dict[word] = [spell]
            
            line = f.readline()

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(header_str)

        for word in spell_dict:
            for spell in spell_dict[word]:
                f.write(word + '\t' + spell + '\n')


if __name__ == '__main__':
    main()
