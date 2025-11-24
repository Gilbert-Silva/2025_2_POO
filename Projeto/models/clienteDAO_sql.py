from models.cliente import Cliente
import sqlite3

class ClienteDAO:
    def __init__(self, db_name="clientes.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def inserir(self, cliente: Cliente):
        self.cursor.execute("""
            INSERT INTO clientes (nome, email, fone, senha)
            VALUES (?, ?, ?, ?)
        """, (cliente.get_nome(), cliente.get_email(),
              cliente.get_fone(), cliente.get_senha()))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT id, nome, email, fone, senha FROM clientes")
        rows = self.cursor.fetchall()
        clientes = [Cliente(id, nome, email, fone, senha) for (id, nome, email, fone, senha) in rows]
        return clientes

    def listar_id(self, id):
        self.cursor.execute("SELECT id, nome, email, fone, senha FROM clientes WHERE id=?", (id,))
        row = self.cursor.fetchone()
        if row:
            return Cliente(*row)
        return None

    def atualizar(self, cliente: Cliente):
        self.cursor.execute("""
            UPDATE clientes SET nome=?, email=?, fone=?, senha=? WHERE id=?
        """, (cliente.get_nome(), cliente.get_email(), cliente.get_fone(),
              cliente.get_senha(), cliente.get_id()))
        self.conn.commit()

    def excluir(self, id):
        self.cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
