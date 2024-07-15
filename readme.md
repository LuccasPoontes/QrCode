# Gerador de QR Code com Logotipo

Este projeto demonstra como gerar um QR Code com um logotipo personalizado em Python usando as bibliotecas `qrcode` e `Pillow`.

## Funcionalidades

- Gerar um QR Code a partir de uma URL ou qualquer texto.
- Adicionar um logotipo personalizado no centro do QR Code.
- Personalizar o tamanho, a borda e o nível de correção de erro do QR Code.

## Pré-requisitos

Certifique-se de que você tem o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

## Instalação

1. Clone o repositório ou baixe o código.
2. Instale as bibliotecas necessárias:

```bash
pip install qrcode[pil]
pip install pillow


Uso
Coloque a imagem do seu logotipo no mesmo diretório do script e nomeie-a como path_to_logo.png.
Atualize o script com o caminho correto para a imagem do seu logotipo.
Execute o script:

import qrcode
from PIL import Image

# Texto ou URL para o QR Code
data = "Follow Love Pratas: - https://www.instagram.com/lpratas_acessorios/?hl=am-et" #Instagram de Diretos Autorais Autorizado pelo proprietário da Lpratas_Acessorios. Link de Exemplo.

# Configuração do QR Code
qr = qrcode.QRCode(
    version=1,  # Controla o tamanho do QR Code (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nível de correção de erro
    box_size=10,  # Tamanho de cada caixa (pixel)
    border=4,  # Tamanho da borda (caixas)
)

# Adicionando dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Criando a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Adicionando um logotipo ao centro do QR Code
logo = Image.open('path_to_logo.png').convert("RGBA")  # Substitua pelo caminho do seu logotipo, essa imagem é exemplo aonde pode ser substituido
logo = logo.resize((60, 60))  # Redimensiona o logotipo

# Criar uma imagem temporária com o QR Code e o logotipo combinados
temp_img = Image.new("RGBA", img.size)
temp_img.paste(img, (0, 0))
temp_img.paste(logo, ((temp_img.size[0] - logo.size[0]) // 2, (temp_img.size[1] - logo.size[1]) // 2), mask=logo)

# Convertendo de volta para RGB
final_img = temp_img.convert("RGB")

# Salvando a imagem do QR Code
final_img.save("enhanced_qr.png")

print("QR code criado com sucesso e salvo como enhanced_qr.png")
```

O QR Code será gerado e salvo como enhanced_qr.png.

### Customização

- Texto ou URL: Altere a variável data para gerar um QR Code para diferentes conteúdos.
- Logotipo: Substitua path_to_logo.png pelo caminho para o seu próprio logotipo.
- Tamanho do QR Code: Ajuste o parâmetro version em QRCode() para mudar o tamanho do QR Code.
- Correção de Erro: Altere o parâmetro error_correction para um dos valores 

  `qrcode.constants.ERROR_CORRECT_L, qrcode.constants.ERROR_CORRECT_M,`

  `qrcode.constants.ERROR_CORRECT_Q ou qrcode.constants.ERROR_CORRECT_H` para diferentes níveis de correção de erro.
- Tamanho da Caixa: Modifique o parâmetro box_size para mudar o tamanho de cada caixa no QR Code.
- Borda: Ajuste o parâmetro border para mudar a espessura da borda ao redor do QR Code.


# Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
### Notas:
- O `README.md` acima fornece uma visão geral abrangente do seu projeto, incluindo instruções de instalação, uso e opções de customização.
- Certifique-se de substituir `'path_to_logo.png'` pelo caminho real da imagem do seu logotipo tanto no script quanto no `README.md`.

Você pode copiar e colar o conteúdo acima no seu arquivo `README.md` no GitHub.
