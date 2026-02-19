import unicurses as uni

## Dibuja una linea hacia la derecha
## si se le pasa false la dibuja hacia la izquierda
def dibujar_linea_h(inicial_x, inicial_y, len, char, der=True):
    if der:
        # toma la distancia entre la posicion inicial en x y la recorre hasta la longitud de la linea
        for i in range(inicial_x, inicial_x+len):
            uni.mvaddstr(inicial_y, i, char)
    else:
        # toma la distancia entre la poscion inicial en x menos la longitud y la recorre hasta la poscion inicial
        for i in range(abs(inicial_x-len), inicial_x):
            uni.mvaddstr(inicial_y, i, char)
    uni.refresh()



def dibujar_linea_v(inicial_x, inicial_y, len, char, arriba=True):
    if not arriba:
        for i in range(inicial_y, inicial_y+len):
            uni.mvaddstr(i, inicial_x, char)
    else:
        for i in range(abs(inicial_y-len), inicial_y):
            uni.mvaddstr(i, inicial_x, char)

    uni.refresh()

# Inicializa la ventana
stdscr  = uni.initscr() ## Inicia la ventana
uni.noecho() ## que no se muestre lo que uno escribe todo el tiempo
uni.cbreak() ## Para evitar el press key pressed
uni.keypad(stdscr, True)
uni.curs_set(0)

LINES , COLS   = uni.getmaxyx(stdscr)
# (LINES - 1) -> Base inferior
# (COLS - 1) -> Limite derecho

uni.start_color()
uni.init_pair(1, uni.COLOR_RED, uni.COLOR_BLACK)
i = 0
while(i < 50):

    uni.mvaddstr((LINES-1), round(COLS/2), 'O')

    for i in range(1, 22):
        dibujar_linea_h(round(COLS/2), LINES-i, round(i*2), 'O')
        dibujar_linea_h(round(COLS/2), LINES-i, round(i*2), 'O', False)
        uni.refresh()
        uni.napms(100)

    dibujar_linea_h(round(COLS/2), LINES-22, round(21*2), 'O')
    dibujar_linea_h(round(COLS/2), LINES-22, round(21*2), 'O', False)
    uni.refresh()
    uni.napms(100)

    for i in range(4, 10):
        dibujar_linea_h(round(COLS*0.35), i, round(i*2.3), 'O')
        dibujar_linea_h(round(COLS*0.35), i, round(i*2.3), 'O', False)
        uni.refresh()
        uni.napms(100)

    for i in range(4, 10):
        dibujar_linea_h(round(COLS*0.65), i, round(i*2.3), 'O')
        dibujar_linea_h(round(COLS*0.65), i, round(i*2.3), 'O', False)
        uni.refresh()
        uni.napms(100)

    for i in range(15, 19):
        dibujar_linea_h(round(COLS*0.5), i, 10, ' ')
        dibujar_linea_h(round(COLS*0.5), i, 10, ' ', False)
        uni.refresh()
        uni.napms(100)
    
    uni.attron(uni.COLOR_PAIR(1))
    uni.attron(uni.A_BOLD)

    uni.mvaddstr(16, round(COLS/2), 'T')
    uni.mvaddstr(16, round((COLS/2)+1), 'E')
    uni.refresh()

    uni.mvaddstr(17, round((COLS/2)-2), 'Q')
    uni.mvaddstr(17, round((COLS/2)-1), 'U')
    uni.mvaddstr(17, round(COLS/2), 'I')
    uni.mvaddstr(17, round((COLS/2)+1), 'E')
    uni.mvaddstr(17, round((COLS/2)+2), 'R')
    uni.mvaddstr(17, round((COLS/2)+3), 'O')
    uni.refresh()

    uni.attroff(uni.A_BOLD)
    uni.attroff(uni.COLOR_PAIR(1))

    uni.napms(100)

    i+=1
    

#uni.clrtoeol() -> limpia una linea
# uni.clear() -> limpia la pantalla

# Cierra la ventana
uni.nocbreak()
uni.keypad(stdscr, False)
uni.echo()
uni.endwin()



