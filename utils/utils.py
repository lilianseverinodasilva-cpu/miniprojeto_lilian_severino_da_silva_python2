#Padronização de data de nascimento com Regex

import re

padrao = r"(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})"
texto  = "Data de nascimento: 25/03/1990"

m = re.search(padrao, texto)
if m:
    print(m.group("dia"))  # 25
    print(m.group("mes"))  # 03
    print(m.group("ano"))  # 1990
    print(m.groupdict())   # {'dia': '25', 'mes': '03', 'ano': '1990'}



#função utils prof

def remover_acentos(texto: str) -> str:
    """Remove acentos e caracteres especiais do texto."""
    import unicodedata
    texto_normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto_normalizado if unicodedata.category(c) != "Mn")




#função utils prof

def formatar_cnpj(cnpj: str) -> str:
    """
    Formata um CNPJ para o padrão XX.XXX.XXX/XXXX-XX.

    Exemplo:
        formatar_cnpj("11222333000181") -> "11.222.333/0001-81"
    """
    # Substitui a função 'so_numeros' por essa linha com Regex que remove tudo que não for número:
    cnpj = re.sub(r'\D', '', str(cnpj))
    
    if len(cnpj) != 14:
        raise ValueError(f"CNPJ inválido: esperado 14 dígitos, recebido {len(cnpj)}.")
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"




#Verificar maiúsculas em todos os itesn que são string e object

def verificar_maiusculas_automatico(df):
    print("-" * 100)
    print("   VARREDURA DE STRINGS EM MAIÚSCULAS")
    
    # Este dicionário vai guardar as duas coisas (coluna: total de erros)
    resultado_mapeamento = {}
    
    # Varre apenas colunas object e string
    for coluna in df.select_dtypes(include=['object', 'string']).columns:
        
        # Ignora os nulos para não dar falso positivo
        series_limpa = df[coluna].dropna().astype(str)
        
        if series_limpa.empty:
            continue
            
        # Verifica se existe alguma minúscula/misturada
        if not series_limpa.str.isupper().all():
            # Conta o total de linhas que falharam (usando o operador de negação ~)
            total_nao_maiuscula = (~series_limpa.str.isupper()).sum()
            
            print(f"❌ Coluna '{coluna}': possui valores minúsculos/misturados.")
            print(f"   ↳ Total de termos incorretos: {total_nao_maiuscula:,}".replace(',', '.'))
            
            # Salva no dicionário: a chave é a coluna, o valor é o total
            resultado_mapeamento[coluna] = total_nao_maiuscula
        else:
            print(f"✅ Coluna '{coluna}': está 100% em maiúsculas.")
            
    print("-" * 60)
    
    # RETORNA o dicionário com as duas informações
    return resultado_mapeamento


#Verificador de Falsos Nulos

import pandas as pd
import numpy as np

def encontrar_falsos_nulos(df):
    print("-" * 100)
    print("   🔍 DETECTOR DE FALSOS NULOS (FANTASMAS NA BASE DE DADOS)")
    print("-" * 100)
    
    # Palavras comuns que sistemas usam para fingir que a célula está vazia
    termos_suspeitos = ['NAN', 'NULL', 'NONE', 'N/A', 'EMPTY', '', 'NOT AVAILABLE']
    caracteres_preenchimento = ['-', '.', '?', '*']
    
    colunas_texto = df.select_dtypes(include=['object', 'string']).columns
    total_fantasmas_encontrados = 0

    for coluna in colunas_texto:
        # 1. Conta células que são apenas espaços em branco ou quebras de linha (ex: "   ", "\n")
        apenas_espacos = df[coluna].astype(str).str.match(r'^\s*$').sum()
        
        # 2. Conta palavras textuais como "NaN" ou "Null"
        palavras_vazias = df[coluna].astype(str).str.upper().str.strip().isin(termos_suspeitos).sum()
        
        # 3. Conta caracteres isolados usados para preencher espaço (ex: "-")
        caracteres_isolados = df[coluna].astype(str).str.strip().isin(caracteres_preenchimento).sum()
        
        # Total de falsos nulos na coluna
        total_coluna = apenas_espacos + palavras_vazias + caracteres_isolados
        
        if total_coluna > 0:
            print(f"❌ Coluna '{coluna}' contém potenciais FALSOS NULOS:")
            if apenas_espacos > 0:
                print(f"   ↳ {apenas_espacos:,} linhas preenchidas apenas com ESPAÇOS.".replace(',', '.'))
            if palavras_vazias > 0:
                print(f"   ↳ {palavras_vazias:,} linhas escritas textualmente como 'NaN'/'Null'/'None'.".replace(',', '.'))
            if caracteres_isolados > 0:
                print(f"   ↳ {caracteres_isolados:,} linhas contendo apenas caracteres como '-', '.', '?'.")
            print(f"   [Total na coluna: {total_coluna:,}]\n".replace(',', '.'))
            total_fantasmas_encontrados += total_coluna
            
    if total_fantasmas_encontrados == 0:
        print("✅ Excelente! Nenhum falso nulo foi detetado nas colunas de texto.")
    else:
        print("-" * 100)
        print(f"⚠️ Alerta: Foram encontrados {total_fantasmas_encontrados:,} falsos nulos no total!".replace(',', '.'))
    print("-" * 100)



#Ler o arquivo csv de forma nativa
import csv

def testar_leitura_nativa(caminho_arquivo: str, limitar_linhas: int = 5):
    """
    Realiza a leitura e extração dos arquivos de dados de forma 
    estruturada e nativa utilizando csv.DictReader conforme os critérios do projeto.
    """
    print(f"📖 Iniciando leitura nativa estruturada (DictReader) de: {caminho_arquivo}")
    
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8-sig') as arquivo:
            # O DictReader mapeia as informações de cada linha para um dicionário (chave: valor)
            leitor_dict = csv.DictReader(arquivo)
            
            for i, linha in enumerate(leitor_dict):
                if i >= limitar_linhas:
                    break
                # Exibe a estrutura de dicionário de cada linha
                print(f"🔹 Registro {i+1}: {dict(linha)}")
                
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado no caminho: {caminho_arquivo}")