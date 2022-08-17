def add_space_start_end(string):
  line_split = [*string]
  line_split.append(' ')
  line_split.insert(0, ' ')
  line = ''.join(line_split)
  return line

def load_keys():
  lines = []
  with open('../hot-words.txt','r') as file:
      for line in file:
        stripped_line = line.strip()
        if line[0] == ' ':
          stripped_line = add_space_start_end(stripped_line)
        lines.append(stripped_line)
  return lines