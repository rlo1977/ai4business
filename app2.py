import os
import fitz  # PyMuPDF
from docx import Document

def ler_pdf(caminho_arquivo):
    texto = ""
    try:
        with fitz.open(caminho_arquivo) as pdf:
            for pagina in pdf:
                texto += pagina.get_text()
    except Exception as e:
        print(f"Erro ao ler PDF: {e}")
    return texto

def ler_docx(caminho_arquivo):
    texto = ""
    try:
        doc = Document(caminho_arquivo)
        for paragrafo in doc.paragraphs:
            texto += paragrafo.text + '\n'
    except Exception as e:
        print(f"Erro ao ler DOCX: {e}")
    return texto

def ler_arquivo(caminho):
    if not os.path.exists(caminho):
        return "Arquivo não encontrado."

    extensao = os.path.splitext(caminho)[1].lower()
    if extensao == '.pdf':
        return ler_pdf(caminho)
    elif extensao == '.docx':
        return ler_docx(caminho)
    else:
        return "Formato de arquivo não suportado. Use .pdf ou .docx."

# Exemplo de uso
if __name__ == "__main__":
    caminho_arquivo = input("Informe o caminho completo do arquivo (.pdf ou .docx): ")
    conteudo = ler_arquivo(caminho_arquivo)
    print("\n--- Conteúdo do Arquivo ---\n")
    print(conteudo)
