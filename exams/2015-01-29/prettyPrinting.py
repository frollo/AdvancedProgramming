from functools import reduce

def prettyCSV(filename):
    with open(filename, "r") as f:
        rows = [[x.strip().strip("\"") for x in line.split(";")] for line in f]
    col_length = [reduce(lambda x,y: (x > y and x ) or y, [len(rows[i][j]) for i in range(len(rows))]) for j in range(len(rows[0]))]
    col_format = ["{{!s:<{}}}".format(x) for x in col_length]
    formatted_rows = [ "|" + "|".join(map(lambda x: x[0].format(x[1]), zip(col_format, y))) + "|" for y in rows]
    tot_size = sum(col_length) + len(col_length) + 1
    separator = "".join([ "-" for i in range(tot_size)])
    table = "\n".join([separator] + [formatted_rows[0]] + [separator] + formatted_rows + [separator] )
    print(table)
