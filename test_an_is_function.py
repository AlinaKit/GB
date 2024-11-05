a = 'Hfr123.1'
d = 'hdf2.2'
e = 'bGl2.2'
f = 'h$;a2.1'
g = ''
h = '  '
l = 'df h'
m = 'DFGH'
n = 'Gh H'
o = 'kjH FD'
b = '123.1'
c = '1231'
p = '*'
r = ','
s = '.'
glh = str('!')
print(f'{glh:>25}{a = }; {d = }; {e = };  {f = };    {g = };     {h = };      {l = };   {m = };   {n = };    {o = }; {b = }; {c = }; {p = };   {r = };   {s = }')
print(f'isalnum: {glh:>16}Aa2.2 - {a.isalnum()}, aa2.2 - {d.isalnum()}, aA2.2 - {e.isalnum()}, a@2.2 - {f.isalnum()},    "" - {g.isalnum()}, "   " - {h.isalnum()}, "aaa" - {l.isalnum()}, "AAA" - {m.isalnum()}, "Aaa" - {n.isalnum()}, "aAA" - {o.isalnum()}, 2.2 - {b.isalnum()}, 22 - {c.isalnum()}, "2 2" - {p.isalnum()}, 2 + 2 - {r.isalnum()}, "2+2" - {s.isalnum()}  - только буквы и цифры')
print(f'isalpha: {glh:>16}Aa2.2 - {a.isalpha()}, aa2.2 - {d.isalpha()}, aA2.2 - {e.isalpha()}, a@2.2 - {f.isalpha()},    "" - {g.isalpha()}, "   " - {h.isalpha()}, "aaa" - {l.isalpha()}, "AAA" - {m.isalpha()}, "Aaa" - {n.isalpha()}, "aAA" - {o.isalpha()}, 2.2 - {b.isalpha()}, 22 - {c.isalpha()},"2 2" - {p.isalpha()}, 2 + 2 - {r.isalpha()}, "2+2" - {s.isalpha()} - только буквы')
print(f'isdigit: {glh:>16}Aa2.2 - {a.isdigit()}, aa2.2 - {d.isdigit()}, aA2.2 - {e.isdigit()}, a@2.2 - {f.isdigit()},    "" - {g.isdigit()}, "   " - {h.isdigit()}, "aaa" - {l.isdigit()},"AAA" - {m.isdigit()},"Aaa" - {n.isdigit()},"aAA" - {o.isdigit()}, 2.2 - {b.isdigit()}, 22 - {c.isdigit()}, "2 2" - {p.isdigit()}, 2 + 2 - {r.isdigit()}, "2+2" - {s.isdigit()}  - только цифры')
print(f'isnumeric: {glh:>14}Aa2.2 - {a.isnumeric()}, aa2.2 - {d.isnumeric()}, aA2.2 - {e.isnumeric()}, a@2.2 - {f.isnumeric()},    "" - {g.isnumeric()}, "   " - {h.isnumeric()}, "aaa" - {l.isnumeric()},"AAA" - {m.isnumeric()},"Aaa" - {n.isnumeric()},"aAA" - {o.isnumeric()}, 2.2 - {b.isnumeric()}, 22 - {c.isnumeric()}, "2 2" - {p.isnumeric()}, 2 + 2 - {r.isnumeric()}, "2+2" - {s.isnumeric()}  - только цифры')
print(f'isascii: {glh:>16}Aa2.2 - {a.isascii()},  aa2.2 - {d.isascii()},  aA2.2 - {e.isascii()},  a@2.2 - {f.isascii()},     "" - {g.isascii()},  "   " - {h.isascii()},  "aaa" - {l.isascii()}, "AAA" - {m.isascii()}, "Aaa" - {n.isascii()}, "aAA" - {o.isascii()},  2.2 - {b.isascii()},  22 - {c.isascii()}, "2 2" - {p.isascii()},  2 + 2 - {r.isascii()},  "2+2" - {s.isascii()}  - буквы, цифры, пробел, спецсимволы, матзнаки, точка, пустая строка')
print(f'islower: {glh:>16}Aa2.2 - {a.islower()}, aa2.2 - {d.islower()},  aA2.2 - {e.islower()}, a@2.2 - {f.islower()},     "" - {g.islower()}, "   " - {h.islower()}, "aaa" - {l.islower()}, "AAA" - {m.islower()},"Aaa" - {n.islower()},"aAA" - {o.islower()}, 2.2 - {b.islower()}, 22 - {c.islower()},"2 2" - {p.islower()}, 2 + 2 - {r.islower()}, "2+2" - {s.islower()} - нижний регистр (мал. буквы, цифры, спецсимволы, точка, пробел м/д символами)')
print(f'istitle: {glh:>16}Aa2.2 - {a.istitle()},  aa2.2 - {d.istitle()}, aA2.2 - {e.istitle()}, a@2.2 - {f.istitle()},    "" - {g.istitle()}, "   " - {h.istitle()}, "aaa" - {l.istitle()},"AAA" - {m.istitle()},"Aaa" - {n.istitle()}, "aAA" - {o.istitle()}, 2.2 - {b.istitle()}, 22 - {c.istitle()},"2 2" - {p.istitle()}, 2 + 2 - {r.istitle()}, "2+2" - {s.istitle()} - начинается с большой (только первая в наборе, разделенном пробелом)')
print(f'isupper: {glh:>16}Aa2.2 - {a.isupper()}, aa2.2 - {d.isupper()}, aA2.2 - {e.isupper()}, a@2.2 - {f.isupper()},    "" - {g.isupper()}, "   " - {h.isupper()}, "aaa" - {l.isupper()},"AAA" - {m.isupper()}, "Aaa" - {n.isupper()},"aAA" - {o.isupper()}, 2.2 - {b.isupper()}, 22 - {c.isupper()},"2 2" - {p.isupper()}, 2 + 2 - {r.isupper()}, "2+2" - {s.isupper()} - заглавные буквы')
print(f'isprintable: {glh:>12}Aa2.2 - {a.isprintable()},  aa2.2 - {d.isprintable()},  aA2.2 - {e.isprintable()},  a@2.2 - {f.isprintable()},     "" - {g.isprintable()},  "   " - {h.isprintable()},  "aaa" - {l.isprintable()}, "AAA" - {m.isprintable()}, "Aaa" - {n.isprintable()}, "aAA" - {o.isprintable()},  2.2 - {b.isprintable()},  22 - {c.isprintable()}, "2 2" - {p.isprintable()},  2 + 2 - {r.isprintable()},  "2+2" - {s.isprintable()}  - буквы, цифры, пробел, спецсимволы, матзнаки, точка, пустая строка')
print(f'isspace: {glh:>16}Aa2.2 - {a.isspace()}, aa2.2 - {d.isspace()}, aA2.2 - {e.isspace()}, a@2.2 - {f.isspace()},    "" - {g.isspace()}, "   " - {h.isspace()},  "aaa" - {l.isspace()},"AAA" - {m.isspace()},"Aaa" - {n.isspace()},"aAA" - {o.isspace()}, 2.2 - {b.isspace()}, 22 - {c.isspace()},"2 2" - {p.isspace()}, 2 + 2 - {r.isspace()}, "2+2" - {s.isspace()} - пробел')
