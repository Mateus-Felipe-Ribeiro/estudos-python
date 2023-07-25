# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoDownload = float(input("Tamanho do arquivo para download (MB):"))
velocidadeInternet = float(input("Velocidade link de internet (Mbps):"))
tempoAproximado = (tamanhoDownload / (velocidadeInternet/8)) / 60
print("Tempo aproximado para download:",round(tempoAproximado, 2),"minutos")