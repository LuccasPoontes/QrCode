import qrcode
from PIL import Image

# Texto ou URL para o QR Code
data = "Follow Love Pratas: - https://www.instagram.com/lpratas_acessorios/?hl=am-et"

# Configuração do QR Code
qr = qrcode.QRCode(
    version=1,  # Controle do tamanho do QR Code (1 a 40)
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
logo = Image.open('path_to_logo.png').convert("RGBA")  # Substitua pelo caminho do seu logotipo
logo = logo.resize((60, 60))  # Redimensiona o logotipo

# Criar uma imagem temporária com o QR Code e o logotipo combinados
temp_img = Image.new("RGBA", img.size)
temp_img.paste(img, (0, 0))
temp_img.paste(logo, ((temp_img.size[0] - logo.size[0]) // 2, (temp_img.size[1] - logo.size[1]) // 2), mask=logo)

# Convertendo de volta para RGB
final_img = temp_img.convert("RGB")

# Salvando a imagem do QR Code
final_img = "gerado_qr.png"

print(f"QR code criado com sucesso e salvo como: {final_img}")
