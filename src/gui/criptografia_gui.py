from gi.repository import Gtk
from funcoes.criptografia import criptografia

c = criptografia()

class cripto_janela(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="CriptoKey")

		#Box pai para alinhamento em vertical para adição dos outros box's
		self.vbox = Gtk.VBox()
		self.add(self.vbox)

		# Box's para os elementos
		self.box1 = Gtk.Box()
		self.vbox.pack_start(self.box1, True, True, 10)

		self.box2 = Gtk.VBox()
		self.vbox.pack_start(self.box2, True, True, 10)
		self.box2.set_margin_left(10)
		self.box2.set_margin_right(10)

		self.box3 = Gtk.VBox()
		self.vbox.pack_start(self.box3, True, True, 10)
		self.box3.set_margin_left(10)
		self.box3.set_margin_right(10)

		self.box4 = Gtk.Box()
		self.vbox.pack_start(self.box4, True, True, 10)

		#Elementos
		#Box 1
		self.chave_label = Gtk.Label()
		self.chave_label.set_text("Digite a chave:")
		self.box1.pack_start(self.chave_label, False, False, 10)

		self.chave_entrada = Gtk.Entry()
		self.chave_entrada.set_max_length(16)
		self.chave_entrada.set_width_chars(30)
		self.chave_entrada.set_placeholder_text("Digite a chave aqui...")
		self.box1.pack_start(self.chave_entrada, True, True, 10)

		#Box 2
		self.msg_label = Gtk.Label()
		self.msg_label.set_text("Digite a mensagem a ser (des)criptografada:")
		self.msg_label.set_halign(Gtk.Align.CENTER)
		self.box2.pack_start(self.msg_label, True, True, 0)

		self.msg_entrada = Gtk.Entry()
		self.msg_entrada.set_width_chars(100)
		self.msg_entrada.set_placeholder_text("Digite a mensagem secreta aqui...")
		self.box2.pack_start(self.msg_entrada, True, True, 0)

		#Box 3
		self.msg_saida_label = Gtk.Label()
		self.msg_saida_label.set_text("Saída:")
		self.box3.pack_start(self.msg_saida_label, True, True, 0)

		self.msg_saida = Gtk.Entry()
		self.msg_saida.set_placeholder_text("Saida...")
		self.msg_saida.set_editable(False)
		self.box3.pack_start(self.msg_saida, True, True, 0)

		#Box 4
		self.botao_cripto = Gtk.Button.new_with_label("Criptografar")
		self.botao_cripto.set_halign(Gtk.Align.CENTER)
		self.botao_cripto.connect("clicked", self.botao_cripto_clicado)
		self.botao_cripto.set_size_request(200, 50)
		self.box4.pack_start(self.botao_cripto, True, True, 10)

		self.botao_descripto = Gtk.Button.new_with_label("Descriptografar")
		self.botao_descripto.set_halign(Gtk.Align.CENTER)
		self.botao_descripto.connect("clicked", self.botao_descripto_clicado)
		self.botao_descripto.set_size_request(200, 50)
		self.box4.pack_start(self.botao_descripto, True, True, 10)

	def botao_cripto_clicado(self, button):
		try:
			self.msg_saida.set_text(c.cripto(self.chave_entrada.get_text(), self.msg_entrada.get_text()))
		except Exception as e:
			self.dialogo_erro = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Ops, ocorreu algo de errado...")
			self.dialogo_erro.format_secondary_text("Erro: "+str(e))
			self.dialogo_erro.run()
			self.dialogo_erro.destroy()

	def botao_descripto_clicado(self, button):
		try:
			self.msg_saida.set_text(c.descripto(self.chave_entrada.get_text(), self.msg_entrada.get_text()))
		except Exception as e:
			self.dialogo_erro = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Ops, ocorreu algo de errado...")
			self.dialogo_erro.format_secondary_text("Erro: "+str(e))
			self.dialogo_erro.run()
			self.dialogo_erro.destroy()
