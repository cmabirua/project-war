def longest_common(strs):
    if not strs:
        return ""
    min_length=min(len(string)for string in strs)
    common_prefix=""
    for i in range(min_length):
        char=strs[0][i]
        if all(string[i]==char for string in strs):
            common_prefix += char
        else:
            break
    return common_prefix
strs1=["flower","rat","flight"]
print(longest_common(strs1))
