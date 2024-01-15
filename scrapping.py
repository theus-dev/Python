import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Celulares"

im_human = {'user-agent': 'Chrome/91.0.4472.124'}


def scrape_items(url):
    
    # É utilizado para tentar executar o código como experado, caso não seja, uma mensagem informando que há algum problema é transmitida.
    try:
        # Recebe o código da requisição HTTPS GET
        response = requests.get(url, headers = im_human)

        # O construtor da biblioteca é chamado, recebendo como parâmetros a resposta da requisição.
        # Perceba que o código só é verificado sob a condição da requisição ser bem sucedida.
        # O atributo .text contém o conteúdo da resposta, ou seja, o conteúdo HTML da página web que foi baixado.
        # O segundo atributo representa o parser escolhido, no caso o parser nativo do Python.
        soup = BeautifulSoup(response.text, 'html.parser')

        # O objeto a ser verificado é encontrado pela sua classe. Muitas vezes, a classe é um boa escolha pois
        # Todos os itens em comum, muitas vezes, irão possuir a mesma classe. Facilitando a seleção de itens específicos
        smarthPhone_class = 'sc-fBWQRz cULVBz sc-fulCBj fxxByy sc-heIBml bMUpMo'

        # Localizando o produto com a função find('tag_name', attribute_1='value_1', attribute_2='value_2', ...)
        smartphones_product = soup.find('ul', class_=smarthPhone_class)

        # É verificado se a variável possui algum valor. Caso não, a busca falhou e a variável receberá o valor None,
        # Que nativamente é reconhecido como False.
        if smartphones_product:
            info = [['Smarthphone', 'Preço']]
            for item in smartphones_product.find_all('li', class_='sc-kTbCBX ciMFyT'):
                product_name_tag = item.find('a').find('div', class_='sc-dcjTxL xDJfk').find('h2')
                product_price_tag = item.find('a').find('div', class_='sc-fqkvVR hlqElk sc-bOQTJJ jWlrTP').find('div').find('div').find('p')

                # Verifica se product_name_tag e product_price_tag existem antes de adicioná-los à lista, ou seja, se não são None em tipo.
                if product_name_tag and product_price_tag:
                    info.append([
                        product_name_tag.text.strip(),
                        product_price_tag.text.strip()]
                    )
                else:
                    print("O nome ou o preço dos celulares não foram encontrados.")
            return info
        else:
            print(f"No smartphones with class '{smarthPhone_class}' were found on the page.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Falha ao acessar a página, por favor, verifique se o URL foi digitado corretamente.\n\n\n Erro: {e}")

    except Exception as e:
        print(f"Um erro inesperado aconteceu. Chame o suporte. Erro: {e}")

# URL of the page with the list of items
website_url = 'https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/'

# Get the list of items with names and prices
items_list = scrape_items(website_url)

if items_list:
    for rows in items_list:
        worksheet.append(rows)
        
else:
    print("Não foi possível acessar a lista de itens.")

print('Recolha de dados dos SmartPhones concluída com sucesso!')
workbook.save("Planilha de preços.xlsx")
    


