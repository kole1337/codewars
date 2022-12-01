def decode(s):
    a = 'abdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqH'
    return ''.join(a[(a.find(v)+65-i)%66] if a.find(v)!=-1 else v for i,v in enumerate(s))

#https://www.codewars.com/kata/52cf02cd825aef67070008fa/train/python