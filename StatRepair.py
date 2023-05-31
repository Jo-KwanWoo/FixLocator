class StatRepair:
    def mostsimilarstmt(self, targetloc):
        funName = targetloc[0]
        lineNum = targetloc[1]
        content, start_line_num = inspect.getsourcelines(funName)
        leven = []

        for i in range(start_line_num, start_line_num + len(content)):
            if levenshtein(content[lineNum], content[i]) != 0:
                leven.append(levenshtein(content[lineNum], content[i]))

        dist = leven.index(min(leven))
        line = content[dist]
        ret = (line, dist)
        return ret

            
    def levenshtein(s1, s2, debug=False):
        if len(s1) < len(s2):
            return levenshtein(s2, s1, debug)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))

            if debug:
                print(current_row[1:])

            previous_row = current_row

        return previous_row[-1]

