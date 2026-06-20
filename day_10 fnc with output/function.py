def format_name(f_name,l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    #return formated_fname, formated_lname
    return f"{formated_fname} {formated_lname}" # the result of the function.. it just give the output where the fnc is called

print(format_name('zzv','zzz'))