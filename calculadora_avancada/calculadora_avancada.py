import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math, json, os
from datetime import datetime

CONFIG_FILE = 'calculadora_config.json'

# ==================== CONFIGURAÇÕES ====================
class GerenciadorConfiguracoes:
    def __init__(self):
        self.config = self._carregar_config()

    def _carregar_config(self):
        config_padrao = {
            'historico': [], 
            'memoria': 0, 
            'tema': 'Claro', 
            'precisao_decimais': 10,
            'modo_angulo': 'graus'
        }
            'historico': [], 
            'memoria': 0, 
            'tema': 'Claro', 
            'precisao_decimais': 10,
            'modo_angulo': 'graus'
        }
            'historico': [], 
            'memoria': 0, 
            'tema': 'Claro', 
            'precisao_decimais': 10,
            'modo_angulo': 'graus'
        }
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except: 
                pass
        return config_padrao

    def salvar(self):
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")

# ==================== FUNÇÕES MATEMÁTICAS ====================
class FuncoesMatematicas:
    @staticmethod
    def calcular(expressao):
        contexto = {
            'math': math, 'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos,
            'tan': math.tan, 'log': math.log10, 'ln': math.log, 'pi': math.pi, 'e': math.e,
            '__builtins__': {}
        }
        expressao = (expressao.replace('×', '*').replace('÷', '/')
                                .replace('π', 'pi').replace('²', '**2'))
        return eval(expressao, contexto)

# ==================== CALCULADORA ====================
class Calculadora:
    def __init__(self):
        self.config = GerenciadorConfiguracoes()
        self.janela = tk.Tk()
        self.janela.title("Calculadora Avançada")
        self.janela.geometry("400x500")
        self.janela.minsize(350, 450)

        self.display_var = tk.StringVar(value="0")
        self.expressao_atual, self.ultimo_resultado = "", None
        self.aguardando_operando = False
        self.base_atual = 'DEC'

        self._criar_menu()
        self._criar_interface()
        self._configurar_teclado()
        self._centralizar()

    # ---------------- MENU PRINCIPAL ----------------
    def _criar_menu(self):
        menubar = tk.Menu(self.janela)
        self.janela.config(menu=menubar)
        
        menu_visualizar = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Visualizar", menu=menu_visualizar)
        menu_visualizar.add_command(label="Básica", command=lambda: self.notebook.select(0))
        menu_visualizar.add_command(label="Científica", command=lambda: self.notebook.select(1))
        menu_visualizar.add_command(label="Programador", command=lambda: self.notebook.select(2))
        
        menu_config = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Configurações", menu=menu_config)
        
        menu_angulo = tk.Menu(menu_config, tearoff=0)
        menu_config.add_cascade(label="Modo Ângulo", menu=menu_angulo)
        menu_angulo.add_command(label="Graus", command=lambda: self._alterar_modo_angulo('graus'))
        menu_angulo.add_command(label="Radianos", command=lambda: self._alterar_modo_angulo('radianos'))
        
        menu_ajuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda)
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)

    def _alterar_modo_angulo(self, modo):
        self.config.config['modo_angulo'] = modo
        self.config.salvar()
        self.status_var.set(f"Modo ângulo: {modo}")

    # ---------------- INTERFACE PRINCIPAL ----------------
    def _centralizar(self):
        self.janela.update_idletasks()
        w, h = self.janela.winfo_width(), self.janela.winfo_height()
        x = (self.janela.winfo_screenwidth() - w) // 2
        y = (self.janela.winfo_screenheight() - h) // 2
        self.janela.geometry(f'{w}x{h}+{x}+{y}')

    def _criar_interface(self):
        main = ttk.Frame(self.janela, padding="10")
        main.pack(fill=tk.BOTH, expand=True)

        # Display
        ttk.Entry(main, textvariable=self.display_var, font=('Arial', 20, 'bold'),
                  justify='right', state='readonly').pack(fill=tk.X, ipady=15, pady=(0, 10))

        # Botões de operações rápidas
        botoes_sup = [('C', self.limpar), ('⌫', self.backspace),
                      ('%', self.porcentagem), ('√', self.raiz),
                      ('x²', self.quadrado), ('1/x', self.inverso)]
        frame_sup = ttk.Frame(main); frame_sup.pack(fill=tk.X, pady=(0, 5))
        for i, (txt, cmd) in enumerate(botoes_sup):
            ttk.Button(frame_sup, text=txt, command=cmd).grid(row=0, column=i, sticky='ew', padx=2, pady=2)
            frame_sup.columnconfigure(i, weight=1)

        # Botões principais
        botoes = [
            ['7', '8', '9', '÷'], ['4', '5', '6', '×'],
            ['1', '2', '3', '-'], ['0', '.', '=', '+'],
            ['(', ')', 'π', 'Hist']
        ]
        frame = ttk.Frame(main); frame.pack(fill=tk.BOTH, expand=True)
        for i, linha in enumerate(botoes):
            for j, txt in enumerate(linha):
                cmd = (self.mostrar_historico if txt == 'Hist' 
                       else lambda t=txt: self.clique(t))
                colspan = 2 if txt == '0' else 1
                ttk.Button(frame, text=txt, command=cmd).grid(
                    row=i, column=j, columnspan=colspan, sticky='nsew', padx=1, pady=1)
            frame.rowconfigure(i, weight=1)
        for j in range(4): frame.columnconfigure(j, weight=1)

        # Status
        self.status_var = tk.StringVar(value="Pronto")
        ttk.Label(main, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W).pack(fill=tk.X, pady=(10,0))

    # ---------------- TECLADO ----------------
    def _configurar_teclado(self):
        for i in range(10): self.janela.bind(str(i), lambda e, n=str(i): self.clique(n))
        binds = {'+':'+', '-':'-', '*':'×', '/':'÷', '.':'.', '=':'=',
                 '(': '(', ')': ')'}
        for tecla, simbolo in binds.items():
            self.janela.bind(tecla, lambda e, s=simbolo: self.clique(s))
        self.janela.bind('<Return>', lambda e: self.clique('='))
        self.janela.bind('<BackSpace>', lambda e: self.backspace())
        self.janela.bind('<Escape>', lambda e: self.limpar())

    def clique(self, t):
        try:
            if t.isdigit(): self._digito(t)
            elif t == '.': self._ponto()
            elif t in '+-×÷': self._operador(t)
            elif t == '=': self.calcular()
            elif t == 'π': self.display_var.set(str(math.pi))
            elif t in '()': self.display_var.set(self.display_var.get()+t)
            self.status_var.set(f"Botão: {t}")
        except: self._erro()

    def _digito(self, d):
        atual = self.display_var.get()
        self.display_var.set(d if atual == "0" or self.aguardando_operando else atual+d)
        self.aguardando_operando = False

    def _ponto(self):
        if '.' not in self.display_var.get():
            self.display_var.set(self.display_var.get()+'.')

    def _operador(self, op):
        self.expressao_atual = self.display_var.get() + ' ' + op + ' '
        self.aguardando_operando = True

    def calcular(self):
        try:
            expr = self.expressao_atual + self.display_var.get() if self.expressao_atual else self.display_var.get()
            res = FuncoesMatematicas.calcular(expr)
            if isinstance(res, float) and res.is_integer(): res = int(res)
            self.display_var.set(str(round(res,10)))
            self.ultimo_resultado, self.expressao_atual = res, ""
            self.aguardando_operando = True
            self._historico(expr, res)
            self.status_var.set("Cálculo realizado")
        except: self._erro()

    def _historico(self, expr, res):
        entrada = f"{datetime.now().strftime('%H:%M:%S')}: {expr} = {res}"
        hist = self.config.config['historico']
        hist.append(entrada)
        self.config.config['historico'] = hist[-20:]
        self.config.salvar()

    # ---------------- FUNÇÕES AUX ----------------
    def limpar(self): self.display_var.set("0"); self.expressao_atual = ""; self.aguardando_operando = False
    def backspace(self): self.display_var.set(self.display_var.get()[:-1] or "0")
    def porcentagem(self): self._try(lambda n: n/100)
    def raiz(self): self._try(lambda n: math.sqrt(n) if n>=0 else "Erro")
    def quadrado(self): self._try(lambda n: n**2)
    def inverso(self): self._try(lambda n: 1/n if n!=0 else "Erro")

    def _try(self, func):
        try: self.display_var.set(str(func(float(self.display_var.get()))))
        except: self._erro()

    def _erro(self):
        self.display_var.set("Erro")
        self.status_var.set("Erro no cálculo")

    def mostrar_historico(self):
        w = tk.Toplevel(self.janela); w.title("Histórico"); w.geometry("500x300")
        main = ttk.Frame(w, padding="10"); main.pack(fill=tk.BOTH, expand=True)
        text = scrolledtext.ScrolledText(main, wrap=tk.WORD, font=('Consolas', 10))
        text.pack(fill=tk.BOTH, expand=True, pady=(0,10))
        ttk.Button(main, text="Fechar", command=w.destroy).pack(side=tk.RIGHT)
        for item in reversed(self.config.config['historico']):
            text.insert(tk.END, item+'\n\n')
        text.config(state=tk.DISABLED)

    def mostrar_sobre(self):
        messagebox.showinfo("Sobre", 
            "Calculadora Avançada\n\n"
            "• Modo Básico: Operações fundamentais\n"
            "• Modo Científico: Funções trigonométricas, logaritmos, etc.\n"
            "• Modo Programador: Conversão entre bases numéricas\n\n"
            "Desenvolvido em Python com Tkinter")

    def executar(self): 
        self.janela.mainloop()

# ==================== EXECUÇÃO ====================
if __name__ == "__main__":
    try: 
        print("Iniciando Calculadora Avançada...")
        Calculadora().executar()
    except Exception as e: 
        messagebox.showerror("Erro", f"Não foi possível iniciar: {e}")