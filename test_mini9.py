
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from datetime import date, datetime

@pytest.mark.canal
def test_get_yt_channel():
    # Criando uma instância do webdriver
    driver = webdriver.Firefox()

    driver.get("https://youtube.com/")

    # BUSCA CANAL
    busca = driver.find_element_by_name("search_query")
    busca.send_keys('contrapoints')
    time.sleep(5)
    busca.send_keys(Keys.ENTER)
    time.sleep(5)

    # CLICA NO CANAL
    canal = driver.find_element_by_tag_name("ytd-channel-renderer")
    canal.click()
    time.sleep(5)

    # RECUPERA LINK
    print(driver.current_url)

    assert driver.current_url == "https://www.youtube.com/c/ContraPoints"

    #Fechando navegador
    driver.quit()


@pytest.mark.novo_video
def test_new_video():
    # Criando uma instância do webdriver
    driver = webdriver.Firefox()

    driver.get("https://www.youtube.com/c/ContraPoints")

    # CLICA NA ABA DE VÍDEO
    videos_tab = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]')
    time.sleep(5)
    videos_tab.click()
    time.sleep(5)

    # CLICA NO PRIMEIRO VÍDEO
    video = driver.find_element(By.XPATH, '//*[@id="contents"]/ytd-grid-renderer/div/ytd-grid-video-renderer/div/ytd-thumbnail/a')
    video.click()
    time.sleep(5)

    # VÊ SE DATA DE POSTAGEM É IGUAL A HOJE
    video_date = driver.find_element(By.XPATH, '//*[@id="info-text"]/div[2]/yt-formatted-string').text.lower()

    today = datetime.now()
    dateobj = today.strftime('%b %d, %Y')

    print('video release date:', video_date)
    print("today's date:", dateobj)

    novo = False

    if (video_date == dateobj):
        print('novo vídeo! :)')
        novo = True
    else:
        print('por hora, nada. :(')

    # fechando navegador
    driver.quit()

    # há novo vídeo
    assert novo == True

